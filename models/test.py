from pydantic import BaseModel


class TestBase(BaseModel):
    name: str


class Test(TestBase):
    id: int

    class Config:
        orm_mode = True
