# from fastapi import APIRouter, status
# from api.app import schemas, models
#
# post_router = APIRouter(
#     tags=['Posts'],
#     prefix='/posts',
# )
#
# @post_router.post('', status_code=status.HTTP_201_CREATED)
# async def create_post(post: schemas.PostCreate):
#     return await models.Post.create(**post.dict())
#
#
# @post_router.get('', status_code=status.HTTP_200_OK)
# async def get_posts():
#     return await models.Post.all()