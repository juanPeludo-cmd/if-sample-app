from decimal import Decimal

from app.payroll.service import net_pay


def test_net_pay() -> None:
    assert net_pay(Decimal("1000.00")) == Decimal("790.00")
