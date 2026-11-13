# ADR STORY-202: Holiday pay in payroll

- Status: Accepted
- Date: 2026-11-13
- Story: STORY-202
- Decided at the run's design checkpoint by an architect (the checkpoint record names them). Drafted by the Architecture agent.
- Why an ADR: An ADR is required: the design touches high-risk paths app/payroll/service.py (E16_ADR_RISK)

## Context

As a payroll, I want holiday pay calculated, so that employees taking holidays are paid correctly. It is computed by `app.payroll.service.holiday_pay(gross: Decimal, days: int) -> Decimal`: gross pay times the holiday days, divided by 260 working days, then rounded half up to the cent. Zero days pay 0.00; a negative number of days raises ValueError.

Standards and decisions considered:

- ADR-0001: FastAPI for the HTTP layer (accepted)
- ADR-0002: Money is Decimal, never float (accepted)
- index: Architecture decision records (unknown)
- STD-1: Business rules are plain functions (standard)
- STD-2: Money follows ADR-0002 (standard)
- STD-3: No new dependency or data store without an ADR (standard)
- STD-4: Sensitive areas stay apart (standard)
- STD-5: Interfaces change compatibly (standard)
- STORY-205-late-fee-rate-and-cap-in: ADR STORY-205: Late fee rate and cap in a YAML file finance can edit (accepted)

## Options

### Option 1: Refactor the `holiday_pay` function to comply with the rounding...

Refactor the `holiday_pay` function to comply with the rounding rules and add error handling for negative days.

Components: `app/payroll/service.py`.

- ADR-0001 (FastAPI for the HTTP layer): follows: The function remains within the FastAPI router.
- ADR-0002 (Money is Decimal, never float): follows: All amounts are handled as Decimal with two places.
- index (Architecture decision records): not assessed
- STD-1 (Business rules are plain functions): follows: The function is a pure calculation.
- STD-2 (Money follows ADR-0002): follows: Money follows the ADR for Decimal usage.
- STD-3 (No new dependency or data store without an ADR): n/a: No new dependencies are introduced.
- STD-4 (Sensitive areas stay apart): n/a: No new sensitive areas are introduced.
- STD-5 (Interfaces change compatibly): n/a: No breaking changes to existing interfaces.
- STORY-205-late-fee-rate-and-cap-in (ADR STORY-205: Late fee rate and cap in a YAML file finance can edit): n/a: No ADRs related to this story are affected.

Trade-offs: None

### Option 2: Create a new service function to handle holiday pay, moving the...

Create a new service function to handle holiday pay, moving the calculation logic there and updating the router to call this new function.

Components: `app/payroll/service.py`.

- ADR-0001 (FastAPI for the HTTP layer): follows: The function remains within the FastAPI router.
- ADR-0002 (Money is Decimal, never float): follows: All amounts are handled as Decimal with two places.
- index (Architecture decision records): not assessed
- STD-1 (Business rules are plain functions): follows: The function is a pure calculation.
- STD-2 (Money follows ADR-0002): follows: Money follows the ADR for Decimal usage.
- STD-3 (No new dependency or data store without an ADR): n/a: No new dependencies are introduced.
- STD-4 (Sensitive areas stay apart): n/a: No new sensitive areas are introduced.
- STD-5 (Interfaces change compatibly): n/a: No breaking changes to existing interfaces.
- STORY-205-late-fee-rate-and-cap-in (ADR STORY-205: Late fee rate and cap in a YAML file finance can edit): n/a: No ADRs related to this story are affected.

Trade-offs: None

## Decision

Option 1: Refactor the `holiday_pay` function to comply with the rounding.... Option 1 maintains the existing architecture and only refactors the calculation function, adhering to all the standards and architecture decisions. It keeps the router thin and the calculation logic clean.

## Consequences

The `holiday_pay` function will be correctly implemented and tested, ensuring that it handles different cases, including negative days and rounding correctly. The function will be easy to maintain and extend in the future.

## Related changes

- STORY-202: follows. The change follows the decision to refactor the `holiday_pay` function to comply with rounding rules and add error handling for negative days.
