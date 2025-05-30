from fastapi import APIRouter, Depends, HTTPException
from application.use_cases.create_user import CreateUserUseCase
from application.dtos.user_dto import UserDTO
from infrastructure.repositories.sqlalchemy_user_repository import SQLAlchemyUserRepository
from infrastructure.database.database import AsyncSession, get_db

router = APIRouter()


async def get_user_repository(db: AsyncSession = Depends(get_db)) -> SQLAlchemyUserRepository:
    return SQLAlchemyUserRepository(db)


@router.post("/users/", response_model=UserDTO)
async def create_user(
    name: str,
    email: str,
    user_repository: SQLAlchemyUserRepository = Depends(get_user_repository),
):
    use_case = CreateUserUseCase(user_repository)
    try:
        return await use_case.execute(name, email)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
