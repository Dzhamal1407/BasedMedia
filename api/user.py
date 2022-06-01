from fastapi import APIRouter, status, HTTPException
from . import schemas, utils, models
from tortoise.queryset import Q

user_router = APIRouter(
    tags=['User'],
    prefix="/users"
)


@user_router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
async def create_user(user: schemas.UserCreate):

    if await models.UserModel.filter(Q(email=user.email) | Q(username=user.username)).exists():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )

    if '@' in user.username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="@ symbol is restricted!!!"
        )

    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    return await models.UserModel.create(**user.dict())
