from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str
    published: int


class Item(BaseModel):
    title: str
