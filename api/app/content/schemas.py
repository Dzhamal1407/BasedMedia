from pydantic import BaseModel
from tortoise.contrib.pydantic import PydanticModel, pydantic_model_creator
from . import models


class PostCreate(BaseModel):
    title: str
    content: str
    host_id: int


PostGet = pydantic_model_creator(models.Post)


class PostOut(PydanticModel):
    id: int
    title: str
    content: str
    host_id = int
