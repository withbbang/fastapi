from pydantic import BaseModel


class TestBase(BaseModel):
    name: str


class TestModel(TestBase):
    id: int

    class Config:
        from_attributes = True
