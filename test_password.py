from main import check_password


def test_strong_password():
    result = check_password("Bonjour2026!")
    assert result["strength"] == "Strong"


def test_weak_password():
    result = check_password("abc")
    assert result["strength"] == "Weak"


def test_missing_uppercase():
    result = check_password("bonjour2026!")
    assert result["uppercase"] is False


def test_missing_digit():
    result = check_password("Bonjour!!")
    assert result["digit"] is False
