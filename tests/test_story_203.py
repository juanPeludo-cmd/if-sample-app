from app.auth.keys import check_key
import pytest
from decimal import Decimal

def test_check_key_valid_key():
    """
    AC1: check_key({"X-API-Key": "partner-key-1"}, "partner-key-1") returns True
    """
    assert check_key({"X-API-Key": "partner-key-1"}, "partner-key-1") == True

def test_check_key_invalid_key():
    """
    AC2: check_key({"X-API-Key": "partner-key-2"}, "partner-key-1") returns False
    """
    assert check_key({"X-API-Key": "partner-key-2"}, "partner-key-1") == False

def test_check_key_empty_headers():
    """
    AC3: check_key({}, "partner-key-1") returns False
    """
    assert check_key({}, "partner-key-1") == False

def test_check_key_empty_key():
    """
    AC4: check_key({"X-API-Key": ""}, "partner-key-1") returns False
    """
    assert check_key({"X-API-Key": ""}, "partner-key-1") == False
