from decimal import Decimal
import pytest
from app.payroll.service import holiday_pay

def test_holiday_pay_ac1():
    """AC1: holiday_pay(Decimal("2600.00"), 5) returns Decimal("50.00")"""
    assert holiday_pay(Decimal("2600.00"), 5) == Decimal("50.00")

def test_holiday_pay_ac2():
    """AC2: holiday_pay(Decimal("1000.00"), 3) returns Decimal("11.54")"""
    assert holiday_pay(Decimal("1000.00"), 3) == Decimal("11.54")

def test_holiday_pay_ac3():
    """AC3: holiday_pay(Decimal("2600.00"), 0) returns Decimal("0.00")"""
    assert holiday_pay(Decimal("2600.00"), 0) == Decimal("0.00")

def test_holiday_pay_ac4():
    """AC4: holiday_pay(Decimal("2600.00"), -1) raises ValueError"""
    with pytest.raises(ValueError):
        holiday_pay(Decimal("2600.00"), -1)
