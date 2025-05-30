from abc import ABC, abstractmethod
from domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    async def save(self, user: User) -> None:
        pass

    @abstractmethod
    async def find_by_id(self, user_id: int) -> User:
        pass
