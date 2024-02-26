from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    item: str

    # TODO: Config - 예시 파라미터
    class Config:
        schema_extra = {"example": {"id": 0, "item": "Example Schema!"}}
