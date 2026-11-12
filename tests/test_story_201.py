import pytest
from decimal import Decimal
from app.invoices import reminder_fee

def test_reminder_fee_zero_and_fifteen_days():
    """AC1: reminder_fee(0) returns Decimal("0.00") and reminder_fee(14) returns Decimal("0.00")"""
    assert reminder_fee(0) == Decimal("0.00")
    assert reminder_fee(14) == Decimal("0.00")

def test_reminder_fee_fifteen_and_forty_four_days():
    """AC2: reminder_fee(15) returns Decimal("5.00") and reminder_fee(44) returns Decimal("5.00")"""
    assert reminder_fee(15) == Decimal("5.00")
    assert reminder_fee(44) == Decimal("5.00")

def test_reminder_fee_forty_five_and_four_hundred_days():
    """AC3: reminder_fee(45) returns Decimal("10.00") and reminder_fee(400) returns Decimal("10.00")"""
    assert reminder_fee(45) == Decimal("10.00")
    assert reminder_fee(400) == Decimal("10.00")

def test_reminder_fee_negative_days_raises_value_error():
    """AC4: reminder_fee(-1) raises ValueError"""
    with pytest.raises(ValueError):
        reminder_fee(-1)
