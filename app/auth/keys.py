"""Partner API keys (critical: authentication for partner integrations)."""


def check_key(given: str, expected: str) -> bool:
    return given == expected
