from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str
    published: int
    read_times: int


class Item(BaseModel):
    title: str
