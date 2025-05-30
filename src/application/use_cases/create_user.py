from domain.entities.user import User
from domain.value_objects.email import Email
from interfaces.user_repository import UserRepository
from application.dtos.user_dto import UserDTO


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def execute(self, name: str, email: str) -> UserDTO:
        email_obj = Email(email)
        user = User(id=0, name=name, email=email_obj)  # ID will be set by repository
        await self.user_repository.save(user)
        return UserDTO(id=user.id, name=user.name, email=user.email.value)
