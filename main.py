import uvicorn
from fastapi import FastAPI
from routes import test_router, member_router
from database import Base, engine
from middlewares import middlewares


Base.metadata.create_all(bind=engine)

app = FastAPI(middleware=middlewares)


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}


app.include_router(member_router, prefix="/member")
app.include_router(test_router, prefix="/test")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
