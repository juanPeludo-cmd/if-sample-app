import pytest
from decimal import Decimal
from app.invoices import late_fee_settings, late_fee

# AC1: app/late_fee.yaml holds the two settings as `rate: "0.015"` and `cap: "0.10"`
def test_late_fee_settings() -> None:
    expected = {"rate": Decimal("0.015"), "cap": Decimal("0.10")}
    assert late_fee_settings() == expected

# AC2: late_fee_settings() returns {"rate": Decimal("0.015"), "cap": Decimal("0.10")}
def test_late_fee_settings_values() -> None:
    expected = {"rate": Decimal("0.015"), "cap": Decimal("0.10")}
    actual = late_fee_settings()
    assert actual == expected, f"Expected {expected}, but got {actual}"

# AC3: late_fee(Decimal("100.00"), 45) returns Decimal("3.00") and late_fee(Decimal("100.00"), 400) returns Decimal("10.00")
def test_late_fee_calculations() -> None:
    assert late_fee(Decimal("100.00"), 45) == Decimal("3.00")
    assert late_fee(Decimal("100.00"), 400) == Decimal("10.00")
