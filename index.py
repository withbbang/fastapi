import uvicorn
from fastapi import FastAPI
from routes.todo import todo_router
from routes.users import user_router
from routes.events import event_router
from routes.member import member_router
from database.connection import Base, engine
from middlewares.sqlAlchemyMiddleware import SQLAlchemyMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(SQLAlchemyMiddleware)


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}


app.include_router(todo_router)
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")
app.include_router(member_router, prefix="/member")

if __name__ == "__index__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
