from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import AsyncSession
from src.domain.entities.user import User
from src.domain.value_objects.email import Email
from src.interfaces.user_repository import UserRepository
from src.infrastructure.database.database import Base


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)


class SQLAlchemyUserRepository(UserRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, user: User) -> None:
        db_user = UserModel(name=user.name, email=user.email.value)
        self.session.add(db_user)
        await self.session.commit()
        await self.session.refresh(db_user)
        user.id = db_user.id

    async def find_by_id(self, user_id: int) -> User:
        db_user = await self.session.get(UserModel, user_id)
        if not db_user:
            raise UserNotFoundError(f"User with id {user_id} not found")
        return User(id=db_user.id, name=db_user.name, email=Email(db_user.email))
