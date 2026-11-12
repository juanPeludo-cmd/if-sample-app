# ADR STORY-205: Late fee rate and cap in a YAML file finance can edit

- Status: Accepted
- Date: 2026-11-12
- Story: STORY-205
- Decided at the run's design checkpoint by an architect (the checkpoint record names them). Drafted by the Architecture agent.
- Why an ADR: An ADR is required: the design adds app/late_fee.py (E16_ADR_NEW_COMPONENT)

## Context

As finance, I want the late fee's rate and cap kept in `app/late_fee.yaml`, a YAML file we can edit without touching the code, so that a new rate is a one-line change.

Standards and decisions considered:

- ADR-0001: FastAPI for the HTTP layer (accepted)
- ADR-0002: Money is Decimal, never float (accepted)
- index: Architecture decision records (unknown)
- STD-1: Business rules are plain functions (standard)
- STD-2: Money follows ADR-0002 (standard)
- STD-3: No new dependency or data store without an ADR (standard)
- STD-4: Sensitive areas stay apart (standard)
- STD-5: Interfaces change compatibly (standard)

## Options

### Option 1: Modify `app/invoices.py`

Add a new function to read settings from `app/late_fee.yaml` and update `late_fee` to use these settings.

Components: `app/invoices.py`.

- ADR-0001 (FastAPI for the HTTP layer): follows: This option uses FastAPI for the HTTP layer.
- ADR-0002 (Money is Decimal, never float): follows: This option uses Decimal for money calculations.
- index (Architecture decision records): follows: This option adheres to the architecture decision records.
- STD-1 (Business rules are plain functions): follows: This option keeps business rules as plain functions.
- STD-2 (Money follows ADR-0002): follows: This option uses Decimal for money calculations.
- STD-3 (No new dependency or data store without an ADR): follows: This option adds a new third-party package (PyYAML) but has an ADR.
- STD-4 (Sensitive areas stay apart): n/a: This option does not involve sensitive areas.
- STD-5 (Interfaces change compatibly): follows: This option maintains compatibility with existing callers.

Trade-offs: Adds a dependency on PyYAML and introduces a new file to manage settings.

### Option 2: Move late fee logic to a new file

Create a new file `app/late_fee.py` to manage settings and late fee logic.

Components: `app/late_fee.py` (new).

- ADR-0001 (FastAPI for the HTTP layer): follows: This option uses FastAPI for the HTTP layer.
- ADR-0002 (Money is Decimal, never float): follows: This option uses Decimal for money calculations.
- index (Architecture decision records): follows: This option adheres to the architecture decision records.
- STD-1 (Business rules are plain functions): follows: This option keeps business rules as plain functions.
- STD-2 (Money follows ADR-0002): follows: This option uses Decimal for money calculations.
- STD-3 (No new dependency or data store without an ADR): n/a: This option does not add new dependencies.
- STD-4 (Sensitive areas stay apart): n/a: This option does not involve sensitive areas.
- STD-5 (Interfaces change compatibly): follows: This option maintains compatibility with existing callers.

Trade-offs: Introduces a new file to manage settings and late fee logic.

## Decision

Option 2: Move late fee logic to a new file. Option 2 is recommended because it adheres to the repository's standards and does not introduce external dependencies. It keeps the late fee logic and settings management separate, making the codebase cleaner and easier to maintain.

## Consequences

Option 2 will result in a more organized codebase with clear separation of concerns. It will also simplify future updates or modifications to the late fee logic or settings.

## Related changes

- STORY-205: follows. This change follows the decision to move the late fee logic to a new file and manage settings in `app/late_fee.yaml`.
