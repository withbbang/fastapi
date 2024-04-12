import uvicorn
from fastapi import FastAPI
from routes import test_router, member_router
from routes.todo import todo_router  # 삭제 필요
from routes.users import user_router  # 삭제 필요
from routes.events import event_router  # 삭제 필요
from database import Base, engine
from middlewares import middlewares


Base.metadata.create_all(bind=engine)

app = FastAPI(middleware=middlewares)


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}


app.include_router(todo_router)
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")
app.include_router(member_router, prefix="/member")

app.include_router(test_router, prefix="/test")

if __name__ == "__index__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
