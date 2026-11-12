from decimal import Decimal

from app.invoices import late_fee


def test_late_fee_is_zero_when_on_time() -> None:
    assert late_fee(Decimal("100.00"), 0) == Decimal("0.00")


def test_late_fee() -> None:
    assert late_fee(Decimal("100.00"), 31) == Decimal("3.00")


def test_late_fee_is_capped() -> None:
    assert late_fee(Decimal("100.00"), 400) == Decimal("10.00")
