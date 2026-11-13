# ADR STORY-207: Overtime pay in payroll

- Status: Accepted
- Date: 2026-11-13
- Story: STORY-207
- Decided at the run's design checkpoint by an architect (the checkpoint record names them). Drafted by the Architecture agent.
- Why an ADR: An ADR is required: the design touches high-risk paths app/payroll/service.py (E16_ADR_RISK)

## Context

As a payroll, I want overtime pay calculated, so that extra hours are paid correctly.

Standards and decisions considered:

- ADR-0001: FastAPI for the HTTP layer (accepted)
- ADR-0003: Payroll data stays on the client's infrastructure (accepted)
- index: Architecture decision records (unknown)
- STD-1: Business rules are plain functions (standard)
- STD-2: Money follows ADR-0002 (standard)
- STD-3: No new dependency or data store without an ADR (standard)
- STD-4: Sensitive areas stay apart (standard)
- STD-5: Interfaces change compatibly (standard)
- STORY-202-holiday-pay-in-payroll: ADR STORY-202: Holiday pay in payroll (accepted)
- STORY-203-partner-api-keys-from-the-x: ADR STORY-203: Partner API keys from the X-API-Key header (accepted)

## Options

### Option 1: Add a new function `overtime_pay` in `app/payroll/service.py`

Add a new function `overtime_pay` in `app/payroll/service.py`.

Components: `app/payroll/service.py`.

- ADR-0001 (FastAPI for the HTTP layer): follows: FastAPI is already in place for the HTTP layer.
- ADR-0003 (Payroll data stays on the client's infrastructure): follows: Payroll data stays on the client's infrastructure.
- index (Architecture decision records): not assessed
- STD-1 (Business rules are plain functions): follows: Business rules are plain functions.
- STD-2 (Money follows ADR-0002): follows: Money is handled as Decimal.
- STD-3 (No new dependency or data store without an ADR): n/a: No new dependency or data store required.
- STD-4 (Sensitive areas stay apart): follows: Sensitive areas stay apart.
- STD-5 (Interfaces change compatibly): n/a: No interface changes required.
- STORY-202-holiday-pay-in-payroll (ADR STORY-202: Holiday pay in payroll): n/a: Holiday pay ADR is not relevant.
- STORY-203-partner-api-keys-from-the-x (ADR STORY-203: Partner API keys from the X-API-Key header): n/a: Partner API key ADR is not relevant.

Trade-offs: No impact on other components or standards.

### Option 2: Create a new FastAPI router for payroll operations in...

Create a new FastAPI router for payroll operations in `app/payroll/router.py`.

Components: `app/payroll/router.py` (new), `app/payroll/service.py`.

- ADR-0001 (FastAPI for the HTTP layer): follows: FastAPI is already in place for the HTTP layer.
- ADR-0003 (Payroll data stays on the client's infrastructure): follows: Payroll data stays on the client's infrastructure.
- index (Architecture decision records): not assessed
- STD-1 (Business rules are plain functions): follows: Business rules are plain functions.
- STD-2 (Money follows ADR-0002): follows: Money is handled as Decimal.
- STD-3 (No new dependency or data store without an ADR): n/a: No new dependency or data store required.
- STD-4 (Sensitive areas stay apart): follows: Sensitive areas stay apart.
- STD-5 (Interfaces change compatibly): n/a: No interface changes required.
- STORY-202-holiday-pay-in-payroll (ADR STORY-202: Holiday pay in payroll): n/a: Holiday pay ADR is not relevant.
- STORY-203-partner-api-keys-from-the-x (ADR STORY-203: Partner API keys from the X-API-Key header): n/a: Partner API key ADR is not relevant.

Trade-offs: Introduces a new router, but keeps payroll service logic separate.

## Decision

Option 1: Add a new function `overtime_pay` in `app/payroll/service.py`. Option 1 is simpler and more straightforward, directly implementing the overtime pay function in the existing service layer. It follows all architectural and standard guidelines without introducing additional complexity.

## Consequences

Implementing overtime pay calculation in `app/payroll/service.py` keeps the payroll logic centralized and maintains the simplicity of the existing codebase.
