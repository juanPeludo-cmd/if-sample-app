# ADR-0002: Money is Decimal, never float

- Status: Accepted

Floats lose cents. All amounts are `Decimal` with two places, rounded half up, including
`late_fee` and `net_pay`. Code review rejects any float arithmetic on money.

## Related changes

- STORY-201: follows. The `reminder_fee` function uses `Decimal` for calculations, adhering to ADR-0002.
