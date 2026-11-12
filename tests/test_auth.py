from app.auth.keys import check_key


def test_check_key_accepts_the_partner_key() -> None:
    assert check_key("partner-key-1", "partner-key-1")


def test_check_key_refuses_another_key() -> None:
    assert not check_key("partner-key-2", "partner-key-1")
