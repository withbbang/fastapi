import uvicorn
from fastapi import FastAPI
from routes.todo import todo_router
from routes.users import user_router
from routes.events import event_router

app = FastAPI()


@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World"}


app.include_router(todo_router)
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

if __name__ == "__index__":
    uvicorn.run("index:app", host="127.0.0.1", port=8000, reload=True)
