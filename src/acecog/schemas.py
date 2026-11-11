"""JSON Schemas for the Section 7 canonical civic domain objects, plus the process records of Section 8.

These state the TARGET contract from the specification (v0.24; Gate 1 baseline v0.23 plus CL-079 to CL-082), not what the
prototype happens to store today. Each schema carries:

    x-acecog-object   the spec name (Section 7 table)
    x-acecog-phase1   "build" or "interface", from the Phase 1 execution filter (13.6)
    x-acecog-spec     spec sections that define it
    x-acecog-engine   the engine's object_type for this object, or null if the prototype
                      does not store it as a first-class object yet (a gap, see the gap register)

Generated files: docs/api/schemas/<Name>.schema.json  (python scripts/gen_openapi.py)
Contract test:   tests/test_schemas.py validates every object version the engine stores.
"""

DIALECT = "https://json-schema.org/draft/2020-12/schema"
BASE_URI = "https://acecog.org/schemas/v0.24/"

S = {"type": "string"}
NS = {"type": ["string", "null"]}
N = {"type": "number"}
NN = {"type": ["number", "null"]}
B = {"type": "boolean"}
I = {"type": "integer"}
DATE = {"type": ["string", "null"], "description": "ISO 8601 date or date-time."}
IDS = {"type": "array", "items": S}
FRAC = {"type": "number", "minimum": 0, "maximum": 1}


def enum(*v, null=False):
    return {"enum": list(v) + ([None] if null else [])}


def arr(item):
    return {"type": "array", "items": item}


TIERS = ("Provisional", "Vouched", "Documented", "Verified")
GML = {"type": "integer", "minimum": 0, "maximum": 3, "description": "Governance Maturity Level (4.2)."}

# Shared header (Section 7 preamble): identity, version, lifecycle, steward, scope, window,
# provenance, authority basis, confidence, classifications, lineage.
HEADER = {
    "type": "object",
    "required": ["id", "version_id", "object_type", "civic_body_id", "created_in_transaction"],
    "properties": {
        "id": {"type": "string", "description": "Stable identity."},
        "version_id": {"type": "string", "pattern": "@v[0-9]+$", "description": "Immutable version identity: <id>@v<n>."},
        "object_type": S,
        "civic_body_id": {"type": ["string", "null"], "description": "Owning Civic Body; one hash chain per body (CL-068)."},
        "lifecycle_state": NS,
        "owner": NS,
        "scope": NS,
        "effective_from": DATE,
        "effective_to": DATE,
        "authority_basis": {"type": ["string", "null"], "description": "Authority or decision that permitted this version."},
        "confidence": NN,
        "classifications": {"type": "array", "items": S},
        "supersedes": {"type": ["string", "null"], "description": "Prior version this one replaces."},
        "created_in_transaction": {"type": ["string", "null"]},
    },
}

DECISION_CLASS = {
    "type": "object",
    "required": ["name", "method", "approval_threshold", "quorum"],
    "properties": {
        "name": S,
        "method": enum("direct_vote", "consent", "consensus", "supermajority", "delegated"),
        "approval_threshold": FRAC,
        "quorum": FRAC,
        "min_tier": enum(*TIERS),
        "full_confidence_tier": enum(*TIERS),
        "secret_ballot": {"type": "boolean", "description": "Ballot secrecy for this class (CL-069, ASR-07)."},
        "constituency_tags": {"type": "array", "items": S, "description": "Constituencies this class affects (CL-058)."},
        "materiality_threshold": NN,
        "delegation_disclosure_threshold": FRAC,
        "delegation_reconfirm_days": I,
    },
}

# name: (engine object_type or None, phase1, spec refs, required, properties, description)
OBJECTS = {
    "CivicBody": (
        "civic_body", "build", "7, 17.2, 4.2", ["name", "gml_level"],
        {"name": S, "jurisdiction_id": NS, "gml_level": GML, "maturity_framework_id": NS},
        "Self-identifying body of people capable of self-governance."),
    "GovernanceProcess": (
        "governance_process", "build", "7, 17.5, 4.2", ["decision_classes"],
        {"decision_classes": arr(DECISION_CLASS),
         "amendment_threshold": {**FRAC, "description": "Threshold for amending this process; the ratchet applies (invariant 21)."}},
        "Authorized procedure for turning propositions and participation into legitimate decisions."),
    "Jurisdiction": (
        None, "build", "7, 22", ["name"],
        {"name": S, "parent_jurisdiction_id": NS, "boundary": NS, "legal_basis": NS},
        "Self-governing authority boundary."),
    "PortfolioNode": (
        None, "build", "7, 5.2", ["name"],
        {"name": S, "parent_id": NS, "cost": N, "value": N, "depends_on": IDS, "funding_instrument_ids": IDS},
        "Nested governed work, investment or service unit."),
    "Objective": (
        None, "build", "7, 5.3", ["name"],
        {"name": S, "weight": NN, "non_compensable": B, "floor": NN,
         "constituency_tags": IDS},
        "Approved outcome, value or optimization criterion."),
    "Constraint": (
        None, "build", "7, 5.4, 20.1", ["kind", "limit"],
        {"kind": enum("hard", "soft", "floor", "ceiling", "balance"), "limit": N, "applies_to": IDS,
         "evidence_id": NS, "adopted_by_decision_id": NS},
        "Boundary on feasible action or state, with authority and provenance."),
    "Resource": (
        None, "build", "7, 5.5", ["name", "unit", "quantity"],
        {"name": S, "unit": S, "quantity": N, "restricted": B},
        "Scarce or governed quantity."),
    "Relationship": (
        None, "build", "7, 7.1", ["relation", "from_id", "to_id"],
        {"relation": enum("contains", "contributes_to", "constrains", "consumes", "produces", "depends_on",
                          "synergizes_with", "competes_with", "substitutes_for", "externalizes_to", "authorizes",
                          "delegates_to", "funds", "measures", "supersedes", "conflicts_with",
                          "governs_shared_interface"),
         "from_id": S, "to_id": S, "coefficient": NN},
        "Typed connection among objects (7.1)."),
    "Authority": (
        "authority", "build", "7, 12.0.1, 23.1", ["grantee_actor_id", "actions"],
        {"grantee_actor_id": S, "actions": IDS, "monitoring_role": B, "rotation_terms": NS, "recall_terms": NS,
         "revoked": B},
        "Lawful or organizational capacity to approve, prohibit, delegate, waive, commit or execute."),
    "DelegationEnvelope": (
        "delegation_envelope", "build", "5.9, 8.7, 4.2", ["decision_class", "tolerance", "authorized_resolver"],
        {"decision_class": S,
         "tolerance": {"type": "number", "minimum": 0, "description": "T: per-action tolerance (5.9)."},
         "aggregate_tolerance": {"type": ["number", "null"], "minimum": 0,
                                 "description": "Per-period tolerance; default 3 x T in any rolling 30 days (CL-059, CL-060)."},
         "risk_limit": NN, "confidence_threshold": NN, "min_reversibility": {"type": ["integer", "null"]},
         "authorized_resolver": NS,
         "valid": {"type": "boolean", "description": "An envelope that fails validation is stored inert, with its errors (5.9)."},
         "validation_errors": IDS},
        "Bounded decision space for a role or computational agent. Only a valid envelope can resolve anything."),
    "Decision": (
        "decision", "build", "7, 8.0, 8.4, 17.4, 23.1.1",
        ["proposition_version_id", "decision_class", "process_version_id", "result", "lifecycle_state", "legal_status"],
        {"proposition_id": S, "proposition_version_id": S, "decision_class": S, "process_version_id": S,
         "result": enum("approved", "rejected", "no_quorum", "tied"), "tally": {"type": "object"},
         "minority_positions": {"type": "array"}, "lifecycle_state": S,
         "legal_status": {"type": "object", "required": ["value"],
                          "properties": {"value": enum("Advisory", "Consultative", "Binding")}},
         "assurance_sensitive": {"type": "boolean", "description": "Margin does not exceed the at-risk count (23.1.1)."},
         "composition_hash": NS},
        "Proposed or completed choice among alternatives."),
    "TreatyCompactAgreement": (
        None, "interface", "7, 22", ["parties"],
        {"parties": IDS, "shared_constraints": IDS, "authorities": IDS},
        "Explicit interface among independent jurisdictions (federation is interface only in Phase 1)."),
    "Evidence": (
        "evidence", "build", "7, 20.1", ["subject", "epistemic_class"],
        {"subject": S, "value": {}, "epistemic_class": enum("Observed", "Reported", "Estimated", "Assumed",
                                                            "Scenario output", "Hypothesis"),
         "confidence": NN, "source": NS},
        "Information about state, performance, effects or conditions."),
    "FundingInstrument": (
        None, "build", "7, 5.13", ["instrument_type", "amount"],
        {"instrument_type": {"enum": ["Appropriation", "Fixed-Rate Debt", "Restricted Grant", "Endowment",
                                      "Collective Enterprise", "Public Finance Institution"],
                             "description": "Phase 1 builds Appropriation only (13.6)."},
         "amount": N, "restrictions": IDS, "steward_id": NS},
        "Governed financial source and restrictions."),
    "ScheduleMilestone": (
        None, "build", "7, 18", ["node_id"],
        {"node_id": S, "duration": NN, "depends_on": IDS, "window_start": DATE, "window_end": DATE,
         "early_start": NN, "early_finish": NN, "late_start": NN, "late_finish": NN, "total_float": NN},
        "Temporal commitment, dependency or window (CPM in 18, MVP-112)."),
    "Risk": (
        None, "build", "7, 21", ["description"],
        {"description": S, "likelihood": NN, "impact": NN, "applies_to": IDS},
        "Uncertainty about a future condition or consequence."),
    "ExceptionProposition": (
        "exception_proposition", "build", "7, 5.11, 8.9", ["governing_conflict", "authority_required", "state"],
        {"governing_conflict": S, "authority_required": S, "failed_tests": IDS, "context": {},
         "state": enum("Routed", "Resolved", "Closed", "Withdrawn"), "cumulative": B},
        "Structured governance question raised by unresolved conflict or infeasibility."),
    "ActorRoleAgent": (
        None, "build", "7, 12.0.1", ["kind", "display_name"],
        {"kind": enum("person", "role", "agent"), "display_name": S, "roles": IDS,
         "accountability_path": NS, "approval_track_record": {"type": ["object", "null"]}},
        "Identity or function capable of acting; authentication is not authority."),
    "MembershipCredential": (
        "membership_credential", "build", "7, 17.5, 23.1.1", ["member_actor_id", "tier"],
        {"member_actor_id": S, "identity_id": NS, "tier": enum(*TIERS), "attestation_confidence": FRAC,
         "revoked": B},
        "Governed attestation that an Actor is a unique, eligible member of a Civic Body."),
    "MaturityFramework": (
        None, "build", "7, 4.2, 4.3", ["levels"],
        {"levels": arr({"type": "object", "required": ["level"], "properties": {"level": GML, "controls": IDS}}),
         "reference": B},
        "Graduated institutional rigor; Phase 1 builds GML-0 and GML-1 controls."),
    "FloorRevisionProposal": (
        None, "interface", "7, 14.1", ["classification"],
        {"classification": enum("strengthening", "weakening"), "independent_verification_id": NS},
        "Proposed change to the invariant floor (invariant 20 is interface only)."),
    "EcosystemEntity": (None, "interface", "7, 37", ["name"], {"name": S, "guardian_jurisdiction_id": NS},
                        "Rights-holding ecosystem represented as a legal person (Part V)."),
    "GuardianJurisdiction": (None, "interface", "7, 37", ["ecosystem_entity_id"], {"ecosystem_entity_id": S},
                             "Jurisdiction whose scope is stewardship of an Ecosystem Entity (Part V)."),
    "NaturalCapitalAccount": (None, "interface", "7, 36.2", ["ecosystem_entity_id"],
                              {"ecosystem_entity_id": S, "stocks": {"type": "array"}, "flows": {"type": "array"}},
                              "Ledger of an ecosystem's stocks and flows (Part V)."),
    "StatementOfRelationship": (None, "interface", "7, 38", ["guardian_jurisdiction_id"],
                                {"guardian_jurisdiction_id": S, "text": NS},
                                "Guardian Council's statement of relationship to the land (Part V)."),
    "ResourceCommitmentRegistryEntry": (None, "interface", "7, 41.2", ["resource_id", "quantity"],
                                        {"resource_id": S, "quantity": N, "committed_by": NS},
                                        "Single registration of a committed resource (Part V)."),
    "CompliancePack": (
        "compliance_pack", "build", "7, 43.4", ["pack_id", "edition", "rules"],
        {"pack_id": S, "edition": S, "rules": {"type": "array"}, "module_ids": IDS,
         "composition_hash": {"type": ["string", "null"], "description": "Carried into provenance (CMP-015)."}},
        "Versioned bundle of jurisdiction rules; may only add constraints (invariant 19)."),
    "RetentionSchedule": (
        "retention_schedule", "build", "7, 43.2 ASR-05", ["record_class", "destruction_authority"],
        {"record_class": S,
         "retain_days": {"type": ["integer", "null"], "minimum": 0, "description": "null = permanent (the default, CL-054)."},
         "destruction_authority": S, "legal_basis": NS},
        "Record-class retention periods and destruction authority."),
    "LegalEffectDeclaration": (
        "legal_effect_declaration", "build", "7, 43.2 ASR-08, 8.0",
        ["decision_class", "legal_status", "enabling_authority", "effective_date"],
        {"decision_class": S, "legal_status": enum("Advisory", "Consultative", "Binding"), "enabling_authority": S,
         "effective_date": S, "adopted_by_decision_id": NS, "counsel_opinion_ref": NS},
        "Legal status of a decision class and the authority conferring it (CL-067)."),
    "AcecogIdentity": (
        None, "build", "7, 23.1.1", ["tier"],
        {"tier": enum(*TIERS), "anchor_ids": IDS, "merged_into": NS},
        "One real person within a civic scope, with an assurance tier."),
    "AssuranceAnchor": (
        None, "build", "7, 23.1.1", ["identity_id", "anchor_type", "keyed_hash"],
        {"identity_id": S, "anchor_type": enum("self_assertion", "passkey", "vouching", "document", "registrar"),
         "keyed_hash": NS, "attested_by": IDS},
        "One piece of uniqueness evidence, stored only as a keyed hash."),
    "ReconciliationCase": (
        None, "build", "7, 23.1.1", ["identity_ids", "state"],
        {"identity_ids": IDS, "state": enum("Open", "Merged", "Dismissed"), "recounted_decision_ids": IDS},
        "A suspected duplicate identity under review."),
    "ContinuityOffice": (
        None, "build", "7, 17.9", ["office_type"],
        {"office_type": enum("Justice of the Peace", "Elders Council", "External Convener"), "local_name": NS,
         "holder_ids": IDS, "term_end": DATE},
        "A continuity office configured by a Civic Body; process powers only."),
    "ContinuityCase": (
        None, "build", "7, 17.9", ["condition", "state"],
        {"condition": enum("Absent", "Vacant", "Incapacitated", "Compromised"),
         "state": enum("Detected", "Raised", "Verified", "Convened", "Rolled", "Selected", "Contested", "Certified",
                       "Restored", "Lapsed", "Stalled", "Rejected", "Closed"),
         "initiator_id": NS, "verifier_id": NS, "warrant": {"type": ["object", "null"]}, "sunset_date": DATE},
        "Founding or restoration of an office, from detection to restoration."),
    "ComplianceModule": (
        None, "build", "7, 43.4", ["module_id", "edition", "layer"],
        {"module_id": S, "edition": S, "layer": enum("federal", "state", "local", "body"), "rules": {"type": "array"}},
        "One versioned layer of a Compliance Pack composition."),
    "ControlMapping": (None, "interface", "7, 43.2, 43.5", ["control_id", "framework_control"],
                       {"control_id": S, "framework_control": S, "evidence_template": NS},
                       "Link from an ASR or AI control to an external framework control."),
    "EngagementRecord": (None, "interface", "7, 43.6", ["engagement_type", "fee_basis"],
                         {"engagement_type": enum("operator", "implementer", "auditor"), "fee_basis": S,
                          "staff": IDS},
                         "Operator, implementer or auditor engagement; outcome-linked fees refused."),
    "InterestDeclaration": (
        "interest_declaration", "build", "7, 43.4", ["person_id", "proposition_id", "recusal_status"],
        {"person_id": S, "proposition_id": S, "description": NS, "recusal_status": enum("recused", "cleared")},
        "Declared interest in a proposition; blocks deliberation and voting on it."),
}

# Section 8 process records the engine stores (not Section 7 rows, but part of the contract).
PROCESS_RECORDS = {
    "Proposition": ("proposition", "8.2, 8.3",
                    ["decision_class", "title", "proposer", "state", "bound_process_version"],
                    {"decision_class": S, "title": S, "body": NS, "requested_action": {}, "competes_with": NS,
                     "proposer": S, "client": S, "bound_process_version": S,
                     "state": enum("Draft", "Proposed", "Validated", "Returned for correction", "Deliberated",
                                   "Approved", "Rejected", "Superseded", "Withdrawn"),
                     "ai_changes": {"type": "array", "description": "Every AI-introduced change, flagged (INV-AT-15)."}}),
    "Vote": ("vote", "17.3, 17.5", ["proposition_version_id", "voter", "choice"],
             {"proposition_id": S, "proposition_version_id": S, "voter": S, "choice": S, "via_delegate": NS}),
    "Delegation": ("delegation", "17.3, CL-029, CL-064", ["principal", "delegate", "decision_class", "active"],
                   {"principal": S, "delegate": S, "decision_class": S, "active": B, "reconfirm_by_day": I,
                    "assigned_at_seq": I}),
    "DeliberationPost": ("deliberation_post", "8.4, 43.4.1", ["proposition_version_id", "author", "text", "visibility"],
                         {"proposition_id": S, "proposition_version_id": S, "author": S, "text": S,
                          "visibility": enum("public", "private"), "to_actor_id": NS, "position": NS}),
    "PortfolioModel": ("portfolio_model", "5, 13.1", ["budget", "nodes", "objectives", "constraints"],
                       {"budget": N, "nodes": {"type": "array"}, "objectives": {"type": "array"},
                        "constraints": {"type": "array"}}),
    "OptimizationRun": ("optimization_run", "8.6, 13.1, 9.1", ["model_version_id", "config", "state"],
                        {"model_version_id": S,
                         "config": {"type": "object", "required": ["solver", "profile", "lane", "seed"],
                                    "properties": {"solver": S, "profile": S, "lane": S, "seed": I}},
                         "state": S, "result": {}, "rejection": NS}),
    "Baseline": ("baseline", "8.5", ["decision_id", "run_id", "model_version_id", "allocations", "bound_versions"],
                 {"decision_id": S, "run_id": S, "model_version_id": S, "allocations": {},
                  "bound_versions": {"type": "object"}, "reason": NS}),
    "Commitment": ("commitment", "8.7, 19.5", ["baseline_version_id", "amount", "state"],
                   {"baseline_id": S, "baseline_version_id": S, "amount": N, "lines": {"type": "object", "additionalProperties": N, "description": "Amount per portfolio node."},
                    "state": enum("Reserved", "Committed", "Released", "Canceled")}),
    "Actual": ("actual", "8.8", ["node_id", "actual_cost", "baseline_version_id"],
               {"node_id": S, "actual_cost": N, "observed_at": S, "ingested_at": S, "baseline_version_id": S,
                "variance": N}),
    "ConstraintBasis": ("constraint_basis", "20.1", ["constraint_id", "evidence_id", "adopted_by_decision_id"],
                        {"constraint_id": S, "evidence_id": S, "adopted_by_decision_id": S}),
    "Export": ("export", "23.3, ASR-11", ["package_sha256", "event_count"], {"package_sha256": S, "event_count": I}),
    "Setting": ("setting", "43.2, 14.0", [], {}),
}


def _schema(name, engine_type, phase, spec, required, props, desc, section):
    return {
        "$schema": DIALECT,
        "$id": f"{BASE_URI}{name}.schema.json",
        "title": name,
        "description": desc,
        "x-acecog-object": name if section == "8" else _spec_name(name),
        "x-acecog-section": section,
        "x-acecog-phase1": phase,
        "x-acecog-spec": spec,
        "x-acecog-engine": engine_type,
        "allOf": [{"$ref": "ObjectHeader.schema.json"}],
        "type": "object",
        "required": required,
        "properties": props,
    }


_SPEC_NAMES = {"TreatyCompactAgreement": "Treaty / Compact / Agreement", "Evidence": "Evidence / Observation",
               "ScheduleMilestone": "Schedule / Milestone", "ActorRoleAgent": "Actor / Role / Agent",
               "FloorRevisionProposal": "Floor Revision Proposal (FRP)", "AcecogIdentity": "ACECOG Identity"}


def _spec_name(name):
    if name in _SPEC_NAMES:
        return _SPEC_NAMES[name]
    out = ""
    for ch in name:
        out += (" " + ch) if ch.isupper() and out else ch
    return out


CONDITIONS = {
    # A valid envelope must name its resolver and keep its confidence threshold in [0, 1] (5.9).
    "DelegationEnvelope": {"if": {"properties": {"valid": {"const": True}}, "required": ["valid"]},
                           "then": {"properties": {"authorized_resolver": S, "confidence_threshold": FRAC}}},
}


def all_schemas():
    """{file name: schema}. ObjectHeader first; every other schema extends it."""
    out = {"ObjectHeader": {"$schema": DIALECT, "$id": f"{BASE_URI}ObjectHeader.schema.json",
                            "title": "ObjectHeader", "description": "Fields every first-class object carries (Section 7).",
                            **HEADER}}
    for name, (et, phase, spec, req, props, desc) in OBJECTS.items():
        out[name] = _schema(name, et, phase, spec, req, props, desc, "7")
        out[name].update(CONDITIONS.get(name, {}))
    for name, (et, spec, req, props) in PROCESS_RECORDS.items():
        out[name] = _schema(name, et, "build", spec, req, props, f"Process record ({spec}).", "8")
    return out


def by_engine_type():
    return {s["x-acecog-engine"]: s for s in all_schemas().values() if s.get("x-acecog-engine")}
