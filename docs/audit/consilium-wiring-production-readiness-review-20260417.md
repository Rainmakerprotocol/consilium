# Consilium Wiring Production Readiness Review

Date: 2026-04-17
Scope: Initial audit of the Consilium planning documents to assess whether the proposed system wiring is production-ready on paper.
Status: Initial review only. No implementation edits performed.

## Overall Assessment

The current plan set is not yet production-ready as an execution artifact. The main issues are:

- planning document integrity failures
- drift between phase plans and the canonical OpenAPI contract
- non-durable queueing and idempotency assumptions
- incomplete Discord readiness and lifecycle wiring
- weak deployment and validation gates relative to the production claims

## Key Findings

### 1. Planning docs are not reliable machine-readable artifacts yet

Several later-phase planning files fail YAML parsing, which materially weakens confidence in any workflow that assumes these documents are valid structured inputs.

Affected examples:

- `docs/consilium/phase_06_ARCHITECTURE.yaml`
- `docs/consilium/phase_06_IMPLEMENTATION.yaml`
- `docs/consilium/phase_08_ARCHITECTURE.yaml`
- `docs/consilium/phase_08_IMPLEMENTATION.yaml`
- `docs/consilium/phase_09_ARCHITECTURE.yaml`
- `docs/consilium/phase_09_IMPLEMENTATION.yaml`

Related observation:

- `scripts/validate_docs.py` only performs a narrow set of regex checks and does not validate YAML parseability or deeper cross-document consistency.

### 2. Phase plans drift from the canonical API contract

The repo repeatedly states that `consilium-openapi-v1.1.yaml` is authoritative, but the phase plans diverge from it in several important places.

Examples of drift:

- OpenAPI requires `Author.run_id`, while Phase 5 models describe it as optional.
- OpenAPI defines `PostMessageResponse.status` as `created | accepted`, while the phase plans propose queued responses shaped around `status="queued"`.
- OpenAPI defines fetch message fields as `id` and `ts`, while the implementation plans use `message_id` and `timestamp`.
- OpenAPI defines the queued response around `message_ids` and `scheduled_at`, while the phase plans propose `message_id` and `estimated_delay_s`.

This is not only documentation drift. It changes client-visible behavior and would break spec-led integration assumptions.

### 3. Incremental fetch semantics appear to be dropped in Phase 6 wiring

The public contract supports incremental polling with `after_ts`, but the Phase 6 route-update plan explicitly shows the Discord fetch call being made with `None` instead of propagating the cursor.

Effect:

- the fetch endpoint can become contract-incompatible
- polling clients may re-read the entire thread repeatedly
- the deployment narrative for multi-agent collaboration becomes less credible under real load

### 4. Accepted work is not durable across restart or redeploy

The proposed rate-limit queue is an in-memory singleton and the idempotency mechanism is an in-memory TTL cache.

Operational consequence:

- a `202 Accepted` response does not imply durable acceptance
- queued work can be lost on process restart, crash, or deployment
- idempotency state is lost across restarts and only preserved for a short in-process window

For a strict MVP this may be acceptable, but it is not production-grade delivery semantics unless explicitly documented as best-effort only.

### 5. Health and readiness are not clearly tied to Discord availability

The system health endpoint is described as basic and expandable later, while the Discord client connects lazily on demand. That means the service can likely report healthy before Discord is actually connected, authorized, and able to resolve the configured channel.

Operational consequence:

- container health may pass while the core integration dependency is unusable
- deployment platforms may route traffic to an app that cannot create threads or post messages

### 6. Discord channel assumptions are internally inconsistent

Phase 3 describes creating a dedicated text channel for Consilium threads, while the Phase 6 client implementation expects the configured parent channel to be a `ForumChannel`.

This is a wiring incompatibility, not a wording issue.

### 7. Production validation gates are too weak for the stated goal

Later phases rely heavily on symbol-import checks, file existence checks, and manual follow-through. Phase 9 explicitly reduces validation to documentation presence plus optional live checks.

That is not enough evidence for claims like:

- production-ready Discord integration
- deployment-ready health and readiness behavior
- reliable end-to-end multi-agent collaboration wiring

### 8. CORS posture is not aligned with the deployment story

Phase 4 hardcodes same-origin-only behavior, while Phase 9 requires production CORS behavior compatible with Custom GPT integration. The docs acknowledge the need, but do not define an env-driven production allowlist or operational configuration path.

## Evidence Highlights

Files reviewed included:

- `consilium-openapi-v1.1.yaml`
- `scripts/validate_docs.py`
- `docs/consilium/00_TECHNICAL_CONSTRAINTS.yml`
- `docs/consilium/00_VALIDATION_FRAMEWORK.yml`
- `docs/consilium/00_COLLABORATION_PATTERNS.yml`
- `docs/consilium/phase_03_ARCHITECTURE.yaml`
- `docs/consilium/phase_03_IMPLEMENTATION.yaml`
- `docs/consilium/phase_04_IMPLEMENTATION.yaml`
- `docs/consilium/phase_05_ARCHITECTURE.yaml`
- `docs/consilium/phase_05_IMPLEMENTATION.yaml`
- `docs/consilium/phase_06_ARCHITECTURE.yaml`
- `docs/consilium/phase_06_IMPLEMENTATION.yaml`
- `docs/consilium/phase_07_ARCHITECTURE.yaml`
- `docs/consilium/phase_08_ARCHITECTURE.yaml`
- `docs/consilium/phase_08_IMPLEMENTATION.yaml`
- `docs/consilium/phase_09_ARCHITECTURE.yaml`
- `docs/consilium/phase_09_IMPLEMENTATION.yaml`

Supporting command checks performed during the review:

- repo doc validator run: failed on multiple phase documents
- YAML parse checks: failed on representative phase 6, 8, and 9 files

## Question List

1. Are the phase documents intended to be machine-validated, machine-consumable planning artifacts, or only human-readable guidance?
2. Is `consilium-openapi-v1.1.yaml` truly the source of truth, or are later phase plans allowed to redefine public request and response shapes?
3. What is the canonical `202 Accepted` response for queued posts: OpenAPI `accepted/message_ids/scheduled_at`, or the phase-plan `queued/message_id/estimated_delay_s` variant?
4. Should Discord outages surface as `503`, or must public failures remain constrained to the currently documented error responses until the spec is updated?
5. Is `after_ts` required to function end-to-end in production polling flows, and if so why does the Phase 6 route plan drop it when calling the Discord client?
6. What delivery guarantee is intended after returning `202 Accepted`: best-effort only, or durable at-least-once delivery?
7. Should idempotency survive process restart and deployment turnover, or is short-lived in-memory deduplication considered sufficient for the external clients in scope?
8. Should `/v1/system/health` remain green when Discord is disconnected, misconfigured, or unable to resolve the configured parent channel?
9. Is the parent Discord surface a text channel with public threads or a forum channel?
10. Who owns the Discord client lifecycle: FastAPI startup/shutdown hooks, lazy request-time connect, or a separate worker/service model?
11. What concurrency and race assumptions are acceptable for the current singleton in-memory queue design?
12. How should production CORS allowlists be configured for ChatGPT Custom GPT and any browser-based tooling?
13. What evidence is required before calling the wiring production-ready: restart-during-queue tests, Discord outage tests, idempotent retry tests, real readiness checks, or all of them?
14. Is the target really a single-instance MVP with explicit operational caveats, or should Phases 8 and 9 meet a higher reliability bar before being described as production-ready?

## Suggested Next Audit Step

The next useful pass is a subsystem-based review that converts these findings into a production-readiness checklist grouped by:

- API contract compliance
- Discord integration and lifecycle
- queueing and idempotency semantics
- health, observability, and deployment readiness
- validation and test evidence