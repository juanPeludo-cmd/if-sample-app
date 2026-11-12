
from decimal import Decimal

LATE_FEE_RATE = Decimal("0.015")

LATE_FEE_CAP = Decimal("0.10")


def late_fee_settings() -> dict[str, Decimal]:
    return {"rate": LATE_FEE_RATE, "cap": LATE_FEE_CAP}
