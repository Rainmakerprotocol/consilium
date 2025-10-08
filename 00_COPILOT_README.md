# 00_COPILOT_README.md — AI Operations Manual

**Audience:** GitHub Copilot, Jarvis2, Librarian, and other integrated AI agents.  
**Purpose:** Provide deterministic instructions for reading, writing, and validating
within the Consilium Relay repository.

## 1. Project Overview

**Name:** Consilium Relay  
**Purpose:** Enable multi-AI collaboration using Discord as a message board.  
**MVP Definition:** Chairman, Claude, and ChatGPT can all post and read messages in the same Discord thread via the relay service.  
**Runtime:** Python 3.11  
**Framework:** FastAPI  
**Key Dependencies:** FastAPI, discord.py, Pydantic, Uvicorn, pytest.  

**Architecture Summary:**  
- **Left side (API):** REST endpoints `/v1/strategy/start-thread`, `/post`, `/fetch`  
- **Right side (Discord):** Discord client for posting, fetching, splitting messages, and handling rate limits  
- **Middle (Relay):** Core relay logic, attribution embeds, configuration loading, structured logging  


## 2. How to Use This Documentation System

- **Phases:** Work is divided into 9 ordered phases defined in `consilium-9_phase_plan.yml`.  
- **Specs Are Law:** OpenAPI spec (`docs/02_OPENAPI_SCHEMA.yaml`) is the source of truth for endpoints and data models.  
- **Validation Required:** Each phase specifies validation criteria. Outputs must meet these before moving on.  
- **Output Style:** Always generate files at the exact paths defined in the plan. No deviations.  
- **Human vs Copilot Work:** Some phases are manual (e.g., Discord setup). Copilot must not attempt to automate these.  
---

## 3. Repository Context

- The repository follows a **Phase‑0 Governance Model**.  
  Authority order: `00_AI_AGENT_RULES.yml` > `BLUEPRINT` > `ARCHITECTURE` > `IMPLEMENTATION`.
- The **OpenAPI spec** (`consilium-openapi-v1.1.yaml`) is the source of truth.  
  Schema drift constitutes failure.
- Every AI operation must pass the **Validation Framework** defined in `00_VALIDATION_FRAMEWORK.yml`.

---

## 4. Navigation Protocol

| Type | Directory | Purpose |
|------|------------|----------|
| Governance Docs | `/docs/00_parent/` | Phase‑0 standards and rules |
| Phase Files | `/docs/consilium/phase_*` | Active development phases |
| Source Code | `/src/` | Application modules |
| Tests | `/tests/` | Validation suites |
| Container | `Dockerfile`, `docker-compose.yml` | Deployment assets |

AI agents should read files using this order of precedence:
1. `00_AI_AGENT_RULES.yml`
2. `00_PROJECT_MISSION.yml`
3. `00_VALIDATION_FRAMEWORK.yml`
4. Phase‑specific `BLUEPRINT → ARCHITECTURE → IMPLEMENTATION`
5. `TECHNICAL_DECISIONS.yml`
6. `PHASE_NOTES.txt`

---

## 5. Operational Guidelines

- **Tense Management:** Draft = future tense, Complete = past tense.  
- **Spec as Law:** Use `consilium-openapi-v1.1.yaml` for all API generation.  
- **Code Generation:** Maintain 80‑char line length, PEP‑8, type hints, async functions.  
- **CI Compliance:** Run `ruff`, `mypy --strict`, and `pytest` after modifications.  
- **Validation:** Confirm coverage ≥80% for `src/api` and `src/discord`.  
- **Rollback:** Revert using `git checkout -- <affected files>` if CI fails.

---

## 6. Phase Flow Awareness

AI agents should reference `00_PHASE_PROGRESSION.yml` to determine current phase.  
For each phase:
- Read its `BLUEPRINT` and corresponding `ARCHITECTURE` and `IMPLEMENTATION` files.  
- Use the decision links from `00_DECISIONS_INDEX.yml` to ensure consistency.  
- Update progress state in `PHASE_NOTES.txt` upon completion.

---

## 7. Coding Standards

- **Python Conventions:** Follow PEP 8 strictly.  
- **Type Hints:** All functions, methods, and classes must include explicit type hints.  
- **Async:** Use `async def` consistently for FastAPI and discord.py. Never block the event loop.  
- **Line Length:** 80 characters max per line.  
- **Docstrings:** Google-style docstrings for all public functions and classes.  
- **Imports:** Use absolute imports, grouped as stdlib → third-party → local.  


## 8. Codebase Hygiene

- **No Hardcoded Secrets:** All secrets (tokens, IDs, API keys) come from `.env` and load via `src/core/config.py`.  
- **Error Handling:** All endpoints must return structured JSON error objects as defined in the OpenAPI spec.  
- **Logging:** Structured JSON logs including timestamp, level, message, and context. Request IDs required for tracing.  
- **Security:** Validate API key header (`X-Consilium-Api-Key`) on all endpoints.  
- **Testing:** Every new module must include corresponding tests in `tests/`. Minimum 80% coverage target.  


## 9. File Organization Rules

- **Source Code (`src/`):**  
  - `src/api/` → FastAPI routes, schemas, and dependencies  
  - `src/discord/` → Discord client, message handler, rate-limit logic  
  - `src/core/` → Config, logging, shared utilities  
  - `src/main.py` → FastAPI entrypoint  

- **Tests (`tests/`):** Must mirror the structure of `src/`.  
- **Docs (`docs/`):** All specifications and planning documents.  
- **Configs:** `.env.example` documents all required environment variables.  


## 10. Test Expectations

- **Framework:** pytest + pytest-asyncio.  
- **Unit Tests:** Validate small functions (splitter, config loader).  
- **Integration Tests:** End-to-end flows (create thread → post message → fetch messages).  
- **Mocking:** Use pytest-mock to simulate Discord API where appropriate.  
- **Coverage:** >80% for `src/api` and `src/discord`. Coverage checks must pass before deployment.  


## 11. Examples

**✅ Compliant Code Example**  
```python
# src/discord/message_handler.py
async def split_message(content: str, max_length: int = 2000) -> list[str]:
    """
    Splits a Discord message into chunks while preserving code fences.

    Args:
        content: Message content string
        max_length: Maximum characters per Discord message (default 2000)

    Returns:
        List of message chunks
    """
    ...
```

**❌ Non-Compliant Code Example**  
```python
# Bad: missing type hints, no docstring, exceeds line length, hardcoded values
def splitMessage(content):
    return [content[i:i+2000] for i in range(0, len(content), 2000)]
```


## 12. Copilot Instructions

- Always read this document before generating any code.  
- Never deviate from coding standards, hygiene rules, or file organization requirements.  
- Treat `consilium-9_phase_plan.yml` as the authoritative build sequence.  
- Treat `docs/02_OPENAPI_SCHEMA.yaml` as the contract for all APIs.  
- After completing each phase, verify outputs against validation criteria before moving to the next.  
- Ask for clarification only if the specification is ambiguous. Otherwise, assume the spec is complete and binding.  

---

## 13. Communication

- Human developers may leave context in comments within `PHASE_NOTES.txt`.  
- AIs must not overwrite or erase human entries.  
- Always append with timestamped sections under “Agent Updates.”

---

_End of AI Operations Manual._
