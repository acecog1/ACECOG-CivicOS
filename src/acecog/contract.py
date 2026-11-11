"""ACECOG Civic OS API contract, v0.1 (CL-041).

Single source of truth for the server and the generated OpenAPI file.
Every command and query carries the spec sections it implements and the
invariants (Section 14) and controls (43.2) it enforces, so a reviewer can
trace any response back to the specification.
"""

API_VERSION = "0.1.0"
SPEC_VERSION = "ACECOG v0.24"

# ---------------------------------------------------------------- components
STR = {"type": "string"}
ID = {"type": "string", "description": "Stable object identity (Section 7)."}
NUM01 = {"type": "number", "minimum": 0, "maximum": 1}


def ref(name):
    return {"$ref": f"#/components/schemas/{name}"}


SCHEMAS = {
    "LegalStatus": {
        "type": "object",
        "description": "Legal-status axis (8.0, ASR-08). Binding only with a Legal Effect Declaration (invariant 26 ASR-STATUS-001).",
        "required": ["value"],
        "properties": {
            "value": {"enum": ["Advisory", "Consultative", "Binding"]},
            "legal_effect_declaration_id": {"type": ["string", "null"]},
            "enabling_authority": {"type": ["string", "null"]},
            "effective_date": {"type": ["string", "null"]},
        },
    },
    "Status": {
        "type": "object",
        "description": "The four separate status axes every decision, commitment, and published result carries (8.0).",
        "required": ["lifecycle_state", "legal_status", "delivery_readiness", "epistemic_class"],
        "properties": {
            "lifecycle_state": {"enum": ["Draft", "Proposed", "Validated", "Deliberated", "Approved", "Baselined",
                                         "Optimized", "Resolved", "Committed", "Executing", "Measured", "Reconciled",
                                         "Rejected", "Remanded", "Deferred", "Suspended", "Superseded", "Canceled", "Exception"]},
            "legal_status": ref("LegalStatus"),
            "delivery_readiness": {"enum": ["Proposed", "Funded but incomplete", "Operationally verified", "Breached", "Not applicable"]},
            "epistemic_class": {"enum": ["Observed", "Reported", "Estimated", "Assumed", "Scenario output", "Hypothesis", "Not applicable"]},
        },
    },
    "ObjectHeader": {
        "type": "object",
        "description": "Fields every first-class object carries (Section 7 preamble).",
        "required": ["id", "version_id", "object_type", "civic_body_id", "created_in_transaction"],
        "properties": {
            "id": ID,
            "version_id": {"type": "string", "description": "Immutable version identity."},
            "object_type": STR,
            "civic_body_id": {"type": ["string", "null"]},
            "owner": {"type": ["string", "null"]},
            "scope": {"type": ["string", "null"]},
            "effective_from": {"type": ["string", "null"]},
            "effective_to": {"type": ["string", "null"]},
            "authority_basis": {"type": ["string", "null"], "description": "Authority or decision that permitted this version."},
            "confidence": {"type": ["number", "null"]},
            "supersedes": {"type": ["string", "null"], "description": "Prior version this one replaces (lineage)."},
            "created_in_transaction": STR,
        },
    },
    "Refusal": {
        "type": "object",
        "description": "Why a command was refused. Refusals are themselves recorded transactions (8.1).",
        "required": ["code", "reason"],
        "properties": {
            "code": {"enum": [
                "AUTHORITY_MISSING", "AI_CONFIRMATION_REQUIRED", "ELIGIBILITY", "ATTESTATION_TIER", "RECUSED",
                "OPEN_MEETING_GUARD", "LAYER_RULE", "PARTICIPATION_FEE", "SELF_APPOINTMENT", "SCHEMA",
                "NOT_FOUND", "VERSION_CONFLICT", "HARD_CONSTRAINT", "NOT_PSD", "NOT_COMMIT_ELIGIBLE",
                "DOUBLE_ALLOCATION", "BASELINE_IMMUTABLE", "EVIDENCE_NOT_ADOPTED", "RETENTION",
                "ENVELOPE_INVALID", "STATE", "CHANGE_MISMATCH", "CHANGE_ALREADY_APPLIED",
                "APPROVAL_MISMATCH", "APPROVAL_ALREADY_USED", "SELF_GRANT", "WILDCARD_GRANT"]},
            "reason": STR,
            "invariant_id": {"type": ["string", "null"], "description": "Section 14 invariant ID, e.g. GOV-AUTHPATH-001."},
            "control_id": {"type": ["string", "null"], "description": "Assurance Control (43.2) or requirement ID."},
            "conflicting_layer": {"type": ["string", "null"], "description": "Protection layer (14.0) a configuration conflicts with."},
        },
    },
    "Escalation": {
        "type": "object",
        "description": "An action routed to human authority instead of being decided automatically (5.11, 8.7).",
        "required": ["exception_proposition_id", "authority_required", "governing_conflict"],
        "properties": {
            "exception_proposition_id": STR,
            "authority_required": STR,
            "governing_conflict": STR,
            "failed_tests": {"type": "array", "items": STR},
        },
    },
    "CommandEnvelope": {
        "type": "object",
        "description": "Wrapper for every state-changing command (11.6.2). The same envelope is used by every client (11.6.1).",
        "required": ["command_id", "actor_id", "client", "payload"],
        "properties": {
            "command_id": {"type": "string", "description": "Idempotency key: resending the same command_id returns the original result and changes nothing (8.1)."},
            "actor_id": STR,
            "client": {"enum": ["desktop", "assistant", "mobile", "integration"]},
            "human_confirmation": {
                "type": ["object", "null"],
                "description": "Required when client is 'assistant': the human who reviewed and confirmed the drafted command (24.3, UIX-NEUTRAL-002).",
                "properties": {"confirmed_by": STR, "reviewed_payload_hash": STR},
            },
            "payload": {"type": "object"},
        },
    },
    "CommandResult": {
        "type": "object",
        "required": ["transaction_id", "outcome", "bound_versions"],
        "properties": {
            "transaction_id": STR,
            "outcome": {"enum": ["accepted", "refused", "escalated"]},
            "event_ids": {"type": "array", "items": STR},
            "result": {"type": ["object", "null"]},
            "refusal": {"oneOf": [ref("Refusal"), {"type": "null"}]},
            "escalation": {"oneOf": [ref("Escalation"), {"type": "null"}]},
            "bound_versions": {"type": "object", "description": "Versions in force this transaction is bound to (8.9 version binding)."},
            "status": {"oneOf": [ref("Status"), {"type": "null"}]},
        },
    },
    "Event": {
        "type": "object",
        "description": "Entry in the append-only, hash-chained event log (11.3, ASR-04).",
        "required": ["seq", "event_id", "type", "transaction_id", "at", "data", "prev_hash", "hash"],
        "properties": {
            "seq": {"type": "integer"}, "event_id": STR, "type": STR, "transaction_id": STR,
            "at": STR, "data": {"type": "object"}, "prev_hash": STR, "hash": STR,
        },
    },
    "DecisionProvenancePacket": {
        "type": "object",
        "description": "Section 9: everything needed to reconstruct why a decision occurred.",
        "required": ["decision_id", "inputs", "governance", "model", "run", "analysis", "deliberation", "disposition", "outcome", "lineage"],
        "properties": {k: {"type": "object"} for k in ["inputs", "governance", "model", "run", "analysis", "deliberation", "disposition", "outcome", "lineage"]}
        | {"decision_id": STR, "status": ref("Status")},
    },
}

# ------------------------------------------------------------------ payloads
P = {}  # payload schemas per command

P["civic-bodies.create"] = {
    "type": "object", "required": ["name", "founding_members"],
    "properties": {"name": STR, "jurisdiction": STR, "gml_level": {"enum": [0, 1, 2, 3]},
                   "founding_members": {"type": "array", "minItems": 1, "items": {
                       "type": "object", "required": ["actor_id", "display_name"],
                       "properties": {"actor_id": STR, "display_name": STR, "roles": {"type": "array", "items": STR}}}}},
}
P["governance-processes.adopt"] = {
    "type": "object", "required": ["civic_body_id", "decision_classes"],
    "properties": {
        "civic_body_id": STR,
        "decision_classes": {"type": "array", "minItems": 1, "items": {
            "type": "object", "required": ["name", "method", "approval_threshold", "min_attestation"],
            "properties": {
                "name": STR,
                "method": {"enum": ["direct_vote", "consent"]},
                "approval_threshold": NUM01,
                "quorum": NUM01,
                "min_attestation": {"enum": ["self_attested", "verified"],
                                    "description": "Minimum identity tier to take part in this decision class (17.5 eligibility assurance; CL-028)."},
                "min_attestation_confidence": {**NUM01, "description": "Below this, a result is flagged low-confidence and excluded from GML-2+ commitment (invariant 13). Default 0.75."},
                "participation_fee": {"type": "number", "description": "Must be 0; any fee is refused (invariant 24 TRU-ACCESS-001)."},
                "delegation_disclosure_threshold": NUM01,
                "delegation_reconfirm_days": {"type": "integer", "minimum": 1},
            }}},
    },
}
P["authorities.grant"] = {
    "type": "object", "required": ["civic_body_id", "grantee_actor_id", "actions"],
    "properties": {"civic_body_id": STR, "grantee_actor_id": STR,
                   "actions": {"type": "array", "items": STR},
                   "monitoring_role": {"type": "boolean", "description": "Approval or monitoring authority (12.0.1)."},
                   "selected_by_decision_id": {"type": ["string", "null"]},
                   "rotation_terms": {"type": ["string", "null"]}},
}
P["delegation-envelopes.adopt"] = {
    "type": "object", "required": ["civic_body_id", "decision_class", "tolerance"],
    "properties": {"civic_body_id": STR, "decision_class": STR,
                   "tolerance": {"type": "number", "description": "Largest reallocation the envelope may resolve automatically."},
                   "confidence_threshold": {"description": "0-1, default 0.90 (5.9)."},
                   "min_reversibility": {"description": "0-3, default 2 (5.9)."},
                   "authorized_resolver": STR},
}
P["legal-effect-declarations.adopt"] = {
    "type": "object", "required": ["civic_body_id", "decision_class", "legal_status", "enabling_authority"],
    "properties": {"civic_body_id": STR, "decision_class": STR,
                   "legal_status": {"enum": ["Consultative", "Binding"]},
                   "enabling_authority": {"type": "string", "description": "Citation of the law or charter provision that gives the result effect."},
                   "effective_date": STR},
}
P["compliance-packs.adopt"] = {
    "type": "object", "required": ["civic_body_id", "pack_id", "edition", "rules"],
    "properties": {"civic_body_id": STR, "pack_id": STR, "edition": STR,
                   "rules": {"type": "array", "items": {"type": "object", "required": ["rule", "effect"],
                             "properties": {"rule": STR, "effect": {"enum": ["add_constraint", "relax"]},
                                            "legal_basis": STR, "target": STR}}}},
}
P["credentials.issue"] = {
    "type": "object", "required": ["civic_body_id", "member_actor_id", "tier"],
    "properties": {"civic_body_id": STR, "member_actor_id": STR,
                   "tier": {"enum": ["self_attested", "verified"]}, "attestation_confidence": NUM01},
}
P["interest-declarations.record"] = {
    "type": "object", "required": ["civic_body_id", "proposition_id", "description"],
    "properties": {"civic_body_id": STR, "proposition_id": STR, "description": STR},
}
P["delegations.assign"] = {
    "type": "object", "required": ["civic_body_id", "decision_class", "delegate_actor_id"],
    "properties": {"civic_body_id": STR, "decision_class": STR, "delegate_actor_id": STR},
}
P["delegations.revoke"] = {
    "type": "object", "required": ["civic_body_id", "decision_class"],
    "properties": {"civic_body_id": STR, "decision_class": STR},
}
P["propositions.submit"] = {
    "type": "object", "required": ["civic_body_id", "decision_class", "title", "body", "requested_action"],
    "properties": {"civic_body_id": STR, "decision_class": STR, "title": STR, "body": STR,
                   "requested_action": {"type": "object", "description": "Machine-readable action the proposition asks for (17.6), e.g. adopt_portfolio_model."},
                   "competes_with": {"type": ["string", "null"]}},
}
P["propositions.amend"] = {
    "type": "object", "required": ["proposition_id", "body"],
    "properties": {"proposition_id": STR, "body": STR, "requested_action": {"type": "object"}},
}
P["deliberation.post"] = {
    "type": "object", "required": ["proposition_id", "text", "visibility"],
    "properties": {"proposition_id": STR, "text": STR,
                   "visibility": {"enum": ["public", "private"]},
                   "to_actor_id": {"type": ["string", "null"]},
                   "position": {"enum": ["support", "object", "comment", "minority_report"]}},
}
P["votes.cast"] = {
    "type": "object", "required": ["proposition_id", "choice"],
    "properties": {"proposition_id": STR, "choice": {"enum": ["yes", "no", "abstain", "consent", "object"]}},
}
P["decisions.close"] = {
    "type": "object", "required": ["proposition_id"],
    "properties": {"proposition_id": STR},
}
P["evidence.record"] = {
    "type": "object", "required": ["civic_body_id", "subject", "value", "epistemic_class"],
    "properties": {"civic_body_id": STR, "subject": STR, "value": {}, "epistemic_class": SCHEMAS["Status"]["properties"]["epistemic_class"],
                   "confidence": {"type": ["number", "null"]}, "source": STR},
}
P["constraints.attach-evidence"] = {
    "type": "object", "required": ["constraint_id", "evidence_id"],
    "properties": {"constraint_id": STR, "evidence_id": STR, "adopted_by_decision_id": {"type": ["string", "null"]}},
}
P["optimization-runs.request"] = {
    "type": "object", "required": ["civic_body_id", "model_version_id"],
    "properties": {"civic_body_id": STR, "model_version_id": STR,
                   "lane": {"enum": ["strict", "best_effort"], "description": "Strict (commit-eligible) or exploration (9.1)."},
                   "seed": {"type": "integer"},
                   "q_matrix": {"type": ["array", "null"], "description": "Optional pairwise interaction terms; must be positive semidefinite (13.1)."}},
}
P["baselines.create"] = {
    "type": "object", "required": ["decision_id", "run_id"],
    "properties": {"decision_id": STR, "run_id": STR},
}
P["commitments.reserve"] = {
    "type": "object", "required": ["baseline_id"],
    "properties": {"baseline_id": STR},
}
P["actuals.post"] = {
    "type": "object", "required": ["civic_body_id", "node_id", "actual_cost", "observed_at"],
    "properties": {"civic_body_id": STR, "node_id": STR, "actual_cost": {"type": "number"},
                   "observed_at": STR, "attempt_baseline_update": {"type": "boolean"}},
}
P["rebalances.propose"] = {
    "type": "object", "required": ["civic_body_id", "decision_class", "from_node_id", "to_node_id", "amount"],
    "properties": {"civic_body_id": STR, "decision_class": STR, "from_node_id": STR, "to_node_id": STR,
                   "amount": {"type": "number"}, "confidence": {"type": ["number", "null"]},
                   "reversibility": {"type": ["integer", "null"], "minimum": 0, "maximum": 3}},
}
P["exceptions.resolve"] = {
    "type": "object", "required": ["exception_proposition_id", "resolution", "decision_id"],
    "properties": {"exception_proposition_id": STR, "resolution": STR, "decision_id": STR},
}
P["change-requests.put-in-force"] = {
    "type": "object", "required": ["civic_body_id", "target_type", "target_id", "changes", "decision_id"],
    "properties": {"civic_body_id": STR, "target_type": {"enum": ["delegation_envelope", "governance_process"]},
                   "target_id": STR, "changes": {"type": "object"}, "decision_id": STR},
}
P["exports.create"] = {
    "type": "object", "required": ["civic_body_id"], "properties": {"civic_body_id": STR},
}
P["retention-schedules.adopt"] = {
    "type": "object", "required": ["civic_body_id", "record_class", "retain_days", "destruction_authority"],
    "properties": {"civic_body_id": STR, "record_class": STR, "retain_days": {"type": "integer", "minimum": 0},
                   "destruction_authority": STR, "legal_basis": STR},
}
P["records.delete"] = {
    "type": "object", "required": ["record_id", "record_class", "created_days_ago"],
    "properties": {"record_id": STR, "record_class": STR, "created_days_ago": {"type": "integer"},
                   "legal_order": {"type": ["string", "null"]}},
}
P["configuration.set"] = {
    "type": "object", "required": ["civic_body_id", "setting", "value"],
    "properties": {"civic_body_id": STR, "setting": STR, "value": {}},
}

# Plain-language summary, spec refs, enforced rules for each command
COMMANDS = {
    "civic-bodies.create": ("Create a civic body with its founding members.", "7, 17.2, MVP-100", []),
    "governance-processes.adopt": ("Adopt the rules for how each kind of decision is made: method, threshold, and who may take part.", "17.5, 4.2", ["TRU-ACCESS-001", "GOV-AUTHPATH-001"]),
    "authorities.grant": ("Give a person or role the authority to do specific things.", "7, 12.0.1, 23.1", ["GOV-AUTHPATH-001", "TRU-MONITOR-001"]),
    "delegation-envelopes.adopt": ("Set the bounded space inside which routine decisions may be made automatically.", "5.9, 8.7", ["GOV-ENVELOPE-001"]),
    "legal-effect-declarations.adopt": ("Record which law or charter gives a class of decisions legal effect.", "43.2 ASR-08, 8.0", ["ASR-STATUS-001"]),
    "compliance-packs.adopt": ("Adopt a jurisdiction's legal rule bundle. Packs may only add constraints.", "43.4", ["GOV-FRAMEWORK-001"]),
    "credentials.issue": ("Record that a member is a unique, eligible member at an identity tier.", "7, 17.5", ["TRU-ELIG-001", "TRU-ACCESS-001"]),
    "interest-declarations.record": ("Declare a personal interest in a proposition; this blocks deliberating and voting on it.", "43.4, 43.7", ["CMP-004"]),
    "delegations.assign": ("Delegate your participation in a decision class to another member.", "17.3; CL-029", []),
    "delegations.revoke": ("Withdraw a delegation.", "17.3", []),
    "propositions.submit": ("Submit a frozen proposition version for a decision.", "8.3, MVP-101", ["DPP-IMMUTABLE-001", "TRU-ELIG-001"]),
    "propositions.amend": ("Amend a proposition. Creates a new version; the old version stays.", "8.4", ["DPP-IMMUTABLE-001"]),
    "deliberation.post": ("Post to the deliberation record on a proposition.", "8.4, 43.4.1", ["CMP-003", "CMP-004"]),
    "votes.cast": ("Vote or consent on a proposition.", "17.3, 17.5", ["TRU-ELIG-001", "CMP-004"]),
    "decisions.close": ("Close a decision, tally it, and record the Collective Will.", "17.4, 8.4, MVP-102", ["TRU-ELIG-001", "ASR-STATUS-001"]),
    "evidence.record": ("Record evidence with its epistemic class.", "20.1", []),
    "constraints.attach-evidence": ("Use evidence as the basis of a constraint. Uncertain evidence needs a decision first.", "20.1", ["EVD-NORM-001"]),
    "optimization-runs.request": ("Ask the solver for an allocation under the approved model.", "8.6, 13.1, MVP-103", ["OPT-CNST-001", "OPT-REPRO-001", "OPT-NONCOMP-001"]),
    "baselines.create": ("Freeze an approved, commit-eligible result as the baseline.", "8.5", ["OPT-REPRO-001", "GOV-AUTHPATH-001"]),
    "commitments.reserve": ("Reserve resources for the baseline, without double-allocating.", "8.7, 19.5, MVP-104", ["GOV-AUTHPATH-001"]),
    "actuals.post": ("Post what actually happened. Never alters the baseline.", "8.8, MVP-105", ["EXE-BASELINE-001"]),
    "rebalances.propose": ("Propose a routine reallocation. Inside the envelope it is resolved; otherwise it escalates.", "5.9, 8.7, 5.11, MVP-106, MVP-107", ["GOV-ENVELOPE-001", "GOV-EXCEPT-001"]),
    "exceptions.resolve": ("Resolve an Exception Proposition by the authority it names.", "5.11, 8.9, MVP-108", ["GOV-EXCEPT-001", "DPP-IMMUTABLE-001"]),
    "change-requests.put-in-force": ("Put an approved change in force, once, exactly as approved (the decision names the target and a hash of the change). Applies only to transactions that start afterward.", "8.9; CL-046", ["DPP-IMMUTABLE-001", "GOV-AUTHPATH-001"]),
    "exports.create": ("Export everything needed to continue governance elsewhere.", "23.3, ASR-11, MVP-110", ["TRU-EXIT-001"]),
    "retention-schedules.adopt": ("Adopt a records retention period for a record class.", "43.2 ASR-05", []),
    "records.delete": ("Delete a record. Allowed only by schedule or legal order, and recorded.", "43.2 ASR-05, CMP-005", []),
    "configuration.set": ("Change a deployment setting. Settings cannot disable Assurance Controls.", "43.2, 14.0", ["GOV-FRAMEWORK-001"]),
}

QUERIES = {
    "/v0/queries/civic-bodies/{id}": ("Civic body, its members, decision classes, and adopted packs.", "7"),
    "/v0/queries/propositions/{id}": ("Every version of a proposition, deliberation record, and votes.", "8.3, 8.4, MVP-101"),
    "/v0/queries/decisions/{id}": ("A decision with its four status axes.", "8.0"),
    "/v0/queries/decisions/{id}/provenance": ("Decision Provenance Packet.", "9"),
    "/v0/queries/decisions/{id}/replay": ("Replay the decision's optimization from its bound versions and compare hashes.", "9.1, MVP-109"),
    "/v0/queries/baselines/{id}": ("A baseline version and its lineage.", "8.5"),
    "/v0/queries/portfolio/{civic_body_id}": ("Portfolio nodes, budgets, commitments, actuals, and variance.", "5.2, 8.8"),
    "/v0/queries/exceptions/{id}": ("An Exception Proposition: the conflict and the authority required.", "5.11"),
    "/v0/queries/delegations/{civic_body_id}": ("Delegation chains with concentration disclosure.", "17.3; CL-029"),
    "/v0/queries/feed/{actor_id}": ("A member's feed. Every item states why it is shown; order is deterministic.", "11.6.6, UIX-NEUTRAL-003"),
    "/v0/queries/events": ("The hash-chained event log (supports ?after=seq).", "11.3, ASR-04"),
    "/v0/queries/exports/{id}": ("A completed export package.", "ASR-11"),
}
