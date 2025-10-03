# 00_COPILOT_README.md

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


## 3. Coding Standards

- **Python Conventions:** Follow PEP 8 strictly.  
- **Type Hints:** All functions, methods, and classes must include explicit type hints.  
- **Async:** Use `async def` consistently for FastAPI and discord.py. Never block the event loop.  
- **Line Length:** 80 characters max per line.  
- **Docstrings:** Google-style docstrings for all public functions and classes.  
- **Imports:** Use absolute imports, grouped as stdlib → third-party → local.  


## 4. Codebase Hygiene

- **No Hardcoded Secrets:** All secrets (tokens, IDs, API keys) come from `.env` and load via `src/core/config.py`.  
- **Error Handling:** All endpoints must return structured JSON error objects as defined in the OpenAPI spec.  
- **Logging:** Structured JSON logs including timestamp, level, message, and context. Request IDs required for tracing.  
- **Security:** Validate API key header (`X-Consilium-Api-Key`) on all endpoints.  
- **Testing:** Every new module must include corresponding tests in `tests/`. Minimum 80% coverage target.  


## 5. File Organization Rules

- **Source Code (`src/`):**  
  - `src/api/` → FastAPI routes, schemas, and dependencies  
  - `src/discord/` → Discord client, message handler, rate-limit logic  
  - `src/core/` → Config, logging, shared utilities  
  - `src/main.py` → FastAPI entrypoint  

- **Tests (`tests/`):** Must mirror the structure of `src/`.  
- **Docs (`docs/`):** All specifications and planning documents.  
- **Configs:** `.env.example` documents all required environment variables.  


## 6. Test Expectations

- **Framework:** pytest + pytest-asyncio.  
- **Unit Tests:** Validate small functions (splitter, config loader).  
- **Integration Tests:** End-to-end flows (create thread → post message → fetch messages).  
- **Mocking:** Use pytest-mock to simulate Discord API where appropriate.  
- **Coverage:** >80% for `src/api` and `src/discord`. Coverage checks must pass before deployment.  


## 7. Examples

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


## 8. Copilot Instructions

- Always read this document before generating any code.  
- Never deviate from coding standards, hygiene rules, or file organization requirements.  
- Treat `consilium-9_phase_plan.yml` as the authoritative build sequence.  
- Treat `docs/02_OPENAPI_SCHEMA.yaml` as the contract for all APIs.  
- After completing each phase, verify outputs against validation criteria before moving to the next.  
- Ask for clarification only if the specification is ambiguous. Otherwise, assume the spec is complete and binding.  

---
