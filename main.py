import uvicorn
import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from routes import test_router, member_router
from database import Base, engine
from middlewares import middlewares
from database.session import sessionmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Function that handles startup and shutdown events.
    To understand more, read https://fastapi.tiangolo.com/advanced/events/
    """
    yield
    if sessionmanager._engine is not None:
        # Close the DB connection
        await sessionmanager.close()


app = FastAPI(lifespan=lifespan, middleware=middlewares)


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}


app.include_router(member_router, prefix="/member")
app.include_router(test_router, prefix="/test")

if __name__ == "__main__":
    asyncio.run(uvicorn.run(app, host="127.0.0.1", port=8000, reload=True))
