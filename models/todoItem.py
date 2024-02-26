from pydantic import BaseModel
from typing import List


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {"example": {"item": "Read the next chapter of the book"}}


class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos": [{"item": "Example schema 0"}, {"item": "Example schema 1"}]
            }
        }
