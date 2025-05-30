import pytest
from src.domain.entities.user import User
from src.domain.value_objects.email import Email


def test_user_creation():
    email = Email("test@example.com")
    user = User(id=1, name="John Doe", email=email)
    assert user.name == "John Doe"
    assert user.email.value == "test@example.com"


def test_invalid_email_raises_error():
    with pytest.raises(ValueError):
        Email("invalid-email")
