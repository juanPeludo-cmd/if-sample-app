"""Dunning: the next step for an overdue invoice (finance's collection rules)."""

from decimal import Decimal

COLLECTION_MINIMUM = Decimal("50.00")


def dunning_level(days_late: int, amount: Decimal, disputed: bool, reminders_sent: int) -> str:
    """The next step for an invoice: hold, none, reminder, second_reminder, final_notice or
    collection. A disputed invoice is on hold; an amount under the collection minimum never
    goes to collection."""
    if not disputed:
        if days_late > 0:
            if days_late <= 30:
                if reminders_sent == 0:
                    return "reminder"
                else:
                    return "second_reminder"
            else:
                if days_late <= 60:
                    if reminders_sent < 2:
                        return "second_reminder"
                    else:
                        return "final_notice"
                else:
                    if amount >= COLLECTION_MINIMUM:
                        if reminders_sent >= 3:
                            return "collection"
                        else:
                            return "final_notice"
                    else:
                        return "final_notice"
        else:
            return "none"
    else:
        return "hold"
