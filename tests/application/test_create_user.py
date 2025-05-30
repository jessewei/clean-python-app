import pytest
from application.use_cases.create_user import CreateUserUseCase

# from src.application.use_cases.create_user import CreateUserUseCase
from interfaces.user_repository import UserRepository
from domain.entities.user import User
from domain.value_objects.email import Email


class MockUserRepository(UserRepository):
    async def save(self, user: User) -> None:
        user.id = 1

    async def find_by_id(self, user_id: int) -> User:
        return User(id=1, name="John Doe", email=Email("test@example.com"))


@pytest.mark.asyncio
async def test_create_user_use_case():
    repo = MockUserRepository()
    use_case = CreateUserUseCase(repo)
    user_dto = await use_case.execute("John Doe", "test@example.com")
    assert user_dto.id == 1
    assert user_dto.name == "John Doe"
    assert user_dto.email == "test@example.com"
