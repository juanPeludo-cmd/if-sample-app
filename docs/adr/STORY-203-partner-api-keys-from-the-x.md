# ADR STORY-203: Partner API keys from the X-API-Key header

- Status: Accepted
- Date: 2026-11-13
- Story: STORY-203
- Decided at the run's design checkpoint by an architect (the checkpoint record names them). Drafted by the Architecture agent.
- Why an ADR: An ADR is required: the design adds the dependency none (E16_ADR_NEW_DEPENDENCY)

## Context

As a security system, I want partner API keys read from the request headers and compared in constant time, so that keys cannot be guessed by timing.

Standards and decisions considered:

- ADR-0001: FastAPI for the HTTP layer (accepted)
- ADR-0002: Money is Decimal, never float (accepted)
- index: Architecture decision records (unknown)
- STD-1: Business rules are plain functions (standard)
- STD-2: Money follows ADR-0002 (standard)
- STD-3: No new dependency or data store without an ADR (standard)
- STD-4: Sensitive areas stay apart (standard)
- STD-5: Interfaces change compatibly (standard)
- STORY-202-holiday-pay-in-payroll: ADR STORY-202: Holiday pay in payroll (accepted)
- STORY-205-late-fee-rate-and-cap-in: ADR STORY-205: Late fee rate and cap in a YAML file finance can edit (accepted)

## Options

### Option 1: Use FastAPI's dependency injection to inject the API key into the...

Use FastAPI's dependency injection to inject the API key into the request, then compare it in constant time.

Components: `app/auth/keys.py`, `app/main.py`.

- ADR-0001 (FastAPI for the HTTP layer): follows: FastAPI's dependency injection adheres to the standard.
- ADR-0002 (Money is Decimal, never float): n/a: No money handling in this option.
- index (Architecture decision records): n/a: No new components added.
- STD-1 (Business rules are plain functions): n/a: No new business rules added.
- STD-2 (Money follows ADR-0002): n/a: No new money handling.
- STD-3 (No new dependency or data store without an ADR): n/a: No new dependencies.
- STD-4 (Sensitive areas stay apart): n/a: No sensitive areas added.
- STD-5 (Interfaces change compatibly): n/a: No changes to existing interfaces.
- STORY-202-holiday-pay-in-payroll (ADR STORY-202: Holiday pay in payroll): n/a: No changes to holiday pay calculation.
- STORY-205-late-fee-rate-and-cap-in (ADR STORY-205: Late fee rate and cap in a YAML file finance can edit): n/a: No changes to late fee rate and cap.

Trade-offs: Slightly more complex setup with dependency injection, but adheres to security best practices.

### Option 2: Use a custom middleware to extract the API key from the headers...

Use a custom middleware to extract the API key from the headers and compare it in constant time.

Components: `app/auth/keys.py`, `app/main.py`.

- ADR-0001 (FastAPI for the HTTP layer): follows: FastAPI's middleware can be used to adhere to the standard.
- ADR-0002 (Money is Decimal, never float): n/a: No money handling in this option.
- index (Architecture decision records): n/a: No new components added.
- STD-1 (Business rules are plain functions): n/a: No new business rules added.
- STD-2 (Money follows ADR-0002): n/a: No new money handling.
- STD-3 (No new dependency or data store without an ADR): n/a: No new dependencies.
- STD-4 (Sensitive areas stay apart): n/a: No sensitive areas added.
- STD-5 (Interfaces change compatibly): n/a: No changes to existing interfaces.
- STORY-202-holiday-pay-in-payroll (ADR STORY-202: Holiday pay in payroll): n/a: No changes to holiday pay calculation.
- STORY-205-late-fee-rate-and-cap-in (ADR STORY-205: Late fee rate and cap in a YAML file finance can edit): n/a: No changes to late fee rate and cap.

Trade-offs: Slightly less complex than dependency injection, but may not be as clean in terms of separation of concerns.

## Decision

Option 1: Use FastAPI's dependency injection to inject the API key into the.... Option 1 uses FastAPI's dependency injection, which adheres more closely to the ADRs and is generally considered a more modern and flexible approach in FastAPI applications. Option 2 uses middleware, which is simpler but might not be as maintainable or clean.

## Consequences

Following the recommendation will ensure that the API key is read from the request headers and compared in constant time, meeting the security requirements. The chosen approach will also adhere to the repository's architecture and standards.

## Related changes

- STORY-203: follows. The decision follows the recommendation to use FastAPI's dependency injection for reading and comparing API keys in constant time.
