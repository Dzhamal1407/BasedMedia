from pydantic import BaseModel
from tortoise.contrib.pydantic import PydanticModel, pydantic_model_creator
from fastapi import UploadFile, File, Form
from typing import Type, Optional
import inspect
from . import models
from ..user.schemas import UserPublic


def as_form(cls: Type[BaseModel]):
    """
    Adds an as_form class method to decorated models. The as_form class method
    can be used with FastAPI endpoints
    """
    new_params = [
        inspect.Parameter(
            field.alias,
            inspect.Parameter.POSITIONAL_ONLY,
            default=(Form(field.default) if not field.required else Form(...)),
            annotation=field.outer_type_,
        )
        for field in cls.__fields__.values()
    ]

    async def _as_form(**data):
        return cls(**data)

    sig = inspect.signature(_as_form)
    sig = sig.replace(parameters=new_params)
    _as_form.__signature__ = sig
    setattr(cls, "as_form", _as_form)
    return cls


@as_form
class PostCreate(BaseModel):
    title: str
    content: str
    image: Optional[UploadFile]
    host_id: int


PostGet = pydantic_model_creator(models.Post)


class PostOut(PydanticModel):
    id: int
    title: str
    content: str
    image: Optional[str]
    host: UserPublic
