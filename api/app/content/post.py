import json
import os

from fastapi import APIRouter, status, Form, Depends, UploadFile, File
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from . import schemas, service
from typing import List
from pydantic import ValidationError

post_router = APIRouter(
    tags=['Posts'],
    prefix='/posts',
)


@post_router.post('', status_code=status.HTTP_201_CREATED)
async def create_post(post: schemas.PostCreate = Depends(schemas.PostCreate.as_form)):
    return await service.post_s.create_post(post)


@post_router.get('', status_code=status.HTTP_200_OK, response_model=List[schemas.PostOut])
async def get_all_posts():
    return await service.post_s.all()


@post_router.get('/{pk}', status_code=status.HTTP_200_OK, response_model=schemas.PostOut)
async def get_post_details(pk: int):
    return await service.post_s.get_obj(id=pk)
