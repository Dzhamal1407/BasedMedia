from fastapi import APIRouter, status
from . import schemas, service
from typing import List

post_router = APIRouter(
    tags=['Posts'],
    prefix='/posts',
)


@post_router.post('', status_code=status.HTTP_201_CREATED, response_model=schemas.PostOut)
async def create_post(post: schemas.PostCreate):
    return await service.post_s.create(post)


@post_router.get('', status_code=status.HTTP_200_OK, response_model=List[schemas.PostGet])
async def get_all_posts():
    return await service.post_s.all()


@post_router.get('/{pk}', status_code=status.HTTP_200_OK, response_model=schemas.PostOut)
async def get_post_details(pk: int):
    return await service.post_s.get_obj(id=pk)
