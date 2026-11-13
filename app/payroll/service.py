"""Payroll runs. CONFIDENTIAL: salaries never leave the client's infrastructure (ADR-0003)."""

from decimal import Decimal

from fastapi import APIRouter, HTTPException

from app.db import get_session
from app.models import PayrollEntry
from decimal import ROUND_HALF_UP

router = APIRouter(prefix="/payroll")

TAX_RATE = Decimal("0.21")


def net_pay(gross: Decimal) -> Decimal:
    return (gross * (1 - TAX_RATE)).quantize(Decimal("0.01"))


@router.post("/run")
def run_payroll() -> dict[str, str]:
    session = get_session()
    entries = session.query(PayrollEntry).all()
    total = sum((net_pay(e.gross) for e in entries), Decimal("0"))
    session.execute("UPDATE payroll_entries SET paid = 1")
    return {"paid": str(total)}


@router.get("/holiday-pay")
def read_holiday_pay(gross: Decimal, days: int) -> dict[str, str]:
    """Holiday pay for a gross pay and a number of days; 501 until `holiday_pay` exists."""
    pay = globals().get("holiday_pay")
    if pay is None:
        raise HTTPException(501, "not implemented yet")
    try:
        return {"gross": str(gross), "days": str(days), "holiday_pay": str(pay(gross, days))}
    except ValueError as exc:
        raise HTTPException(400, str(exc)) from exc


def holiday_pay(gross: Decimal, days: int) -> Decimal:
    if days < 0:
        raise ValueError("Number of days cannot be negative")
    if days == 0:
        return Decimal("0.00")
    return (gross * days / Decimal("260")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
