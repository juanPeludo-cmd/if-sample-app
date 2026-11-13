"""Partner API keys (critical: authentication for partner integrations)."""

import hashlib
import time


def check_key(headers: dict[str, str], expected: str) -> bool:
    given = headers.get("X-API-Key", "")
    if not given:
        return False

    # Use a constant-time comparison
    start_time = time.perf_counter()
    result = hashlib.sha256(given.encode()).hexdigest() == hashlib.sha256(expected.encode()).hexdigest()
    end_time = time.perf_counter()

    # Ensure the comparison takes constant time
    elapsed_time = end_time - start_time
    if elapsed_time > 0.01:  # 10 milliseconds is an arbitrary threshold for constant time
        return False

    return result
