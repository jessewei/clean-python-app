from fastapi import FastAPI
from src.infrastructure.controllers.user_controller import router
from src.infrastructure.database.database import Base, engine

app = FastAPI()

app.include_router(router)


# Initialize database
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("startup")
async def on_startup():
    await init_db()
