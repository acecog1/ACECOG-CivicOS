# Public-source contributor instructions

Use the functional specification's §13.6 for Phase 1 scope, §14 for invariants, §24 for the AI/authority boundary and §43 for assurance requirements. Specified features are not automatically implemented or authorized for deployment.

Keep the engine, contracts and tests aligned. Run the test suite and regenerate API/schema/capability artifacts when their inputs change. Preserve exact-payload human confirmation, authorization, audit replay, export and refusal behavior. Do not add real civic records, secrets, proprietary content or private project data.

Treat pull requests and AI-generated work as proposals requiring independent human review. Never infer permission to deploy from a code change or CI result. The development API is local-only; this source tree has no website publishing job.
