"""Synthetic contract tests; fixtures are never release attestations."""
import json
from pathlib import Path
import tempfile
import unittest
from zipfile import ZipFile, ZipInfo
from scripts import bg2_publication_gate as gate


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.archive = self.root / 'candidate.zip'
        self.decision = self.root / 'decision.json'
        self.sha = 'a' * 40
        self.files = {'index.html': b'Unchanged BG-1 fixture',
            'beta/index.html': b'<a href="./legal/index.html">Notices</a>',
            'beta/legal/index.html': b'Synthetic notice page',
            'beta/legal/SOURCE_ACCESS.txt': b'Synthetic source instructions',
            'beta/legal/THIRD_PARTY_NOTICES.txt': b'Synthetic full notices',
            'beta/legal/claims.json': json.dumps({'claims': [{
                'id': 'fixture-only', 'classification': 'M', 'disposition': 'SATISFIED',
                'evidence_paths': ['beta/legal/THIRD_PARTY_NOTICES.txt']}]}).encode()}

    def write(self):
        manifest = {'schema': gate.SCHEMA, 'source_sha': self.sha,
            'bg1_file_sha256': {'index.html': gate.digest(self.files['index.html'])},
            'file_sha256': {n: gate.digest(b) for n, b in self.files.items()}}
        self.manifest = json.dumps(manifest).encode()
        with ZipFile(self.archive, 'w') as z:
            for n, b in self.files.items():
                z.writestr(n, b)
            z.writestr('publication-manifest.json', self.manifest)
        self.archive_hash = gate.digest(self.archive.read_bytes())
        self.approval = {'schema': 'ACECOG-BG2-INDEPENDENT-DECISION-v1',
            'source_sha': self.sha, 'archive_sha256': self.archive_hash,
            'manifest_sha256': gate.digest(self.manifest),
            'claims_sha256': gate.digest(self.files['beta/legal/claims.json']),
            'mandatory_groups': {n: 'CLOSED' for n in gate.GROUPS}}
        for role in ('independent_qa', 'security_licensing', 'qualified_human'):
            self.approval[role] = {'decision': 'ACCEPT', 'reviewer': 'SYNTHETIC TEST ONLY',
                                  'evidence_url': 'https://example.invalid/test-only'}
        self.pin_decision()

    def pin_decision(self):
        self.decision.write_text(json.dumps(self.approval))
        self.decision_hash = gate.digest(self.decision.read_bytes())

    def verify(self):
        return gate.require_publication_artifact(self.archive, source_sha=self.sha,
            archive_sha256=self.archive_hash, decision=self.decision,
            decision_sha256=self.decision_hash)

    def test_valid_exact_bytes_have_positive_path(self):
        self.write()
        self.assertEqual(self.verify()['source_sha'], self.sha)

    def test_no_out_of_band_decision_cannot_pass(self):
        self.write()
        with self.assertRaisesRegex(RuntimeError, 'protected'):
            gate.require_publication_artifact(self.archive)

    def test_changed_archive_even_self_consistent_is_rejected(self):
        self.write()
        old_hash = self.archive_hash
        self.files['beta/index.html'] += b'modified'
        self.write()
        self.archive_hash = old_hash
        with self.assertRaisesRegex(RuntimeError, 'archive bytes'):
            self.verify()

    def test_changed_decision_is_rejected_without_new_protected_pin(self):
        self.write()
        self.decision.write_text(self.decision.read_text() + ' ')
        with self.assertRaisesRegex(RuntimeError, 'decision bytes'):
            self.verify()

    def test_pending_group_or_missing_independent_disposition_is_rejected(self):
        for field in ('mandatory_groups', 'security_licensing', 'independent_qa'):
            with self.subTest(field=field):
                self.write()
                self.approval.pop(field)
                self.pin_decision()
                with self.assertRaises(RuntimeError):
                    self.verify()

    def test_formal_legal_review_is_final_qa_not_initial_publication(self):
        self.write()
        self.approval.pop('qualified_human')
        self.pin_decision()
        self.assertEqual(self.verify()['source_sha'], self.sha)

    def test_unknown_and_pending_claims_do_not_become_residual(self):
        for kind, status in [('U', 'ACCEPTED_RESIDUAL'), ('M', 'PENDING'), ('R', 'PENDING')]:
            with self.subTest(kind=kind):
                self.files['beta/legal/claims.json'] = json.dumps({'claims': [{
                    'id': 'fixture-only', 'classification': kind, 'disposition': status,
                    'evidence_paths': ['beta/legal/THIRD_PARTY_NOTICES.txt']}]}).encode()
                self.write()
                with self.assertRaises(RuntimeError):
                    self.verify()

    def test_missing_notices_fail_even_with_recomputed_inventory(self):
        del self.files['beta/legal/THIRD_PARTY_NOTICES.txt']
        self.write()
        with self.assertRaisesRegex(RuntimeError, 'missing recipient'):
            self.verify()

    def test_inventory_mismatch_extra_missing_and_tampered_payload(self):
        for name, data in [('unexpected.js', b'extra'), ('beta/index.html', b'tampered')]:
            with self.subTest(name=name):
                self.write()
                with ZipFile(self.archive, 'a') as z:
                    z.writestr(name, data)
                self.archive_hash = gate.digest(self.archive.read_bytes())
                with self.assertRaises(RuntimeError):
                    self.verify()

    def test_unsafe_duplicate_case_collision_and_symlink_zip(self):
        for name in ('../escape', '/absolute', 'C:/drive', 'INDEX.HTML', 'index.html'):
            with self.subTest(name=name):
                self.write()
                with ZipFile(self.archive, 'a') as z:
                    z.writestr(name, b'bad')
                with self.assertRaises(RuntimeError):
                    gate.read_archive(self.archive)
        self.write()
        with ZipFile(self.archive, 'a') as z:
            z.writestr('a/b', b'bad')
        # ZipInfo normalizes backslashes on Windows; mutate both filename headers
        # so this tests the actual malformed bytes that an attacker could supply.
        self.archive.write_bytes(self.archive.read_bytes().replace(b'a/b', b'a\\b'))
        with self.assertRaises(RuntimeError):
            gate.read_archive(self.archive)
        self.write()
        with ZipFile(self.archive, 'a') as z:
            info = ZipInfo('symlink')
            info.external_attr = 0o120777 << 16
            z.writestr(info, b'/etc/passwd')
        with self.assertRaises(RuntimeError):
            gate.read_archive(self.archive)

    def test_duplicate_json_keys_rejected(self):
        with self.assertRaisesRegex(RuntimeError, 'duplicate JSON'):
            gate.document(b'{"source_sha":"a","source_sha":"b"}')


if __name__ == '__main__':
    unittest.main()
