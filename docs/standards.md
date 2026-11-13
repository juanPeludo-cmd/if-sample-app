# sample-app engineering standards

The design rules every change is held to, beside the ADRs in `docs/adr/`. A design that
departs from one says so in its ADR, and an architect decides.

## STD-1: Business rules are plain functions

Calculations (fees, totals, pay) are pure functions next to the router that uses them, with
no database or HTTP access, so tests call them directly. Routers stay thin.

## STD-2: Money follows ADR-0002

Every amount is a `Decimal` with two places, rounded half up. No floats, anywhere money is
computed or stored.

## STD-3: No new dependency or data store without an ADR

A new third-party package, table, queue or external service needs its own ADR before it
lands. Prefer the standard library and the existing database.

## STD-4: Sensitive areas stay apart

Payroll and partner keys keep their own packages under `app/`. Other code calls their
public functions and never reads their tables or secrets directly (ADR-0003).

## STD-5: Interfaces change compatibly

An endpoint or public function keeps its existing callers working: new parameters get
defaults, and a breaking change needs a new name or version, plus a note in the ADR.

Reviewed by the team on 2026-11-13.
