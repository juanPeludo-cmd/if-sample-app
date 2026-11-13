import pytest
from app.payroll.service import overtime_pay
from decimal import Decimal

def test_overtime_pay_ac1():
    """AC1: overtime_pay(Decimal("20.00"), 4) returns Decimal("120.00")"""
    assert overtime_pay(Decimal("20.00"), 4) == Decimal("120.00")

def test_overtime_pay_ac2():
    """AC2: overtime_pay(Decimal("15.55"), 3) returns Decimal("69.98")"""
    assert overtime_pay(Decimal("15.55"), 3) == Decimal("69.98")

def test_overtime_pay_ac3():
    """AC3: overtime_pay(Decimal("20.00"), 0) returns Decimal("0.00")"""
    assert overtime_pay(Decimal("20.00"), 0) == Decimal("0.00")

def test_overtime_pay_ac4():
    """AC4: overtime_pay(Decimal("20.00"), -1) raises ValueError"""
    with pytest.raises(ValueError):
        overtime_pay(Decimal("20.00"), -1)
