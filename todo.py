from fastapi import APIRouter
from models.todo import Todo

todo_router = APIRouter()

todo_list = []


@todo_router.post("/todo")
async def say_hello(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}


@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {"todos": todo_list}


@todo_router.get("/todo/{id}")
async def get_single_todo(id: int) -> dict:
    for todo in todo_list:
        if todo.id == id:
            return {"todo": todo}

    return {"message": "Todo with supplied ID doesn't exist"}
