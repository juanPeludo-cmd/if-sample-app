"""Customer statements: the totals finance prints each month (ADR-0002: money is Decimal)."""

from decimal import ROUND_HALF_UP, Decimal

from app.invoices import late_fee


def statement_totals(invoices: list[tuple[Decimal, int]]) -> dict[str, Decimal]:
    """A statement's totals, each rounded to cents: open (not yet due), overdue, the late
    fees on the overdue invoices, and what is due now. Each invoice is (amount, days_late)."""
    open_total = Decimal("0")
    overdue_total = Decimal("0")
    fees = Decimal("0")
    for amount, days_late in invoices:
        if days_late > 0:
            overdue_total += amount
            fees += late_fee(amount, days_late)
        else:
            open_total += amount
    return {
        "open": open_total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        "overdue": overdue_total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        "fees": fees.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        "due": (overdue_total + fees).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
    }
