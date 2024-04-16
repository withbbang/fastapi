import uvicorn
import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from routes import test_router, member_router
from database import Base, engine
from middlewares import middlewares


async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def dispose_database():
    await engine.dispose()


# lifespan 레퍼런스: https://fastapi.tiangolo.com/advanced/events/#alternative-events-deprecated
@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_database()
    yield
    await dispose_database()


app = FastAPI(lifespan=lifespan, middleware=middlewares)


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}


app.include_router(member_router, prefix="/member")
app.include_router(test_router, prefix="/test")

if __name__ == "__main__":
    asyncio.run(uvicorn.run(app, host="127.0.0.1", port=8000, reload=True))
