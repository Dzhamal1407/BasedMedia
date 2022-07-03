from fastapi import APIRouter
from . import oauth2
from ..user import service, schemas
from .schemas import Token

auth_router = APIRouter(
    tags=['Auth'],
    prefix='/auth',
)


@auth_router.post('/login', response_model=Token)
async def login(user_credentials: schemas.UserLogin):

    user = await service.user_s.authenticate(user_credentials)

    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}

