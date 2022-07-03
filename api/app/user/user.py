from fastapi import APIRouter, status, HTTPException
from api.app.user import models, schemas, service


user_router = APIRouter(
    tags=['User'],
    prefix="/users"
)


@user_router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
async def create_user(user: schemas.UserCreate):
    return await service.user_s.create_user(user)
