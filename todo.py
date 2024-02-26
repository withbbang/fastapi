from fastapi import APIRouter, Path
from models.todo import Todo
from models.todoItem import TodoItem

todo_router = APIRouter()

todo_list = []


@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {"message": "Todo added successfully"}


@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {"todos": todo_list}


@todo_router.get("/todo/{id}")
async def get_single_todo(
    id: int = Path(..., title="The ID of the todo to retrieve.")
) -> dict:
    for todo in todo_list:
        if todo.id == id:
            return {"todo": todo}

    return {"message": "Todo with supplied ID doesn't exist"}


@todo_router.put("/todo/{id}")
async def update_todo(
    todo_data: TodoItem, id: int = Path(..., title="The ID of the todo to be updated")
) -> dict:
    for todo in todo_list:
        if todo.id == id:
            todo.item = todo_data.item
            return {"message": "Todo updated successfully."}

    return {"message": "Todo with supplied ID doesn't exist"}


@todo_router.delete("/todo/{id}")
async def delete_single_todo(id: int) -> dict:
    for idx in range(len(todo_list)):
        todo = todo_list[idx]
        if todo.id == id:
            todo_list.pop(idx)
            return {"message": "Todo deleted successfully"}

    return {"message": "Todo with supplied ID doesn't exist"}
