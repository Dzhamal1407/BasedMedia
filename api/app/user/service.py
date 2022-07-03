from ..base.service_base import BaseService
from fastapi import HTTPException, status
from . import schemas, models
from typing import Optional
from tortoise.queryset import Q
from api.app import utils


class UserService(BaseService):
    model = models.UserModel
    create_schema = schemas.UserCreate
    get_schema = schemas.UserOut

    async def create_user(self, schema: schemas.UserCreate) -> Optional[schemas.UserOut]:

        if await self.model.filter(Q(email=schema.email) | Q(username=schema.username)).exists():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User already exists"
            )

        if '@' in schema.username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="@ symbol is restricted!!!"
            )

        hashed_password = utils.hash(schema.password)
        schema.password = hashed_password

        return await models.UserModel.create(**schema.dict())

    async def authenticate(self, schema: schemas.UserLogin):

        user = await self.model.filter(
            Q(email=schema.email_username) |
            Q(username=schema.email_username)
        ).first()

        if not user:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

        if not utils.verify(schema.password, user.password):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

        return user


user_s = UserService()