from fastapi import APIRouter, HTTPException, status
from tortoise.expressions import Q
from . import schemas, oauth2, models, utils
from email_validator import validate_email, EmailNotValidError

auth_router = APIRouter(
    tags=['Auth'],
    prefix='/auth',
)


@auth_router.post('/login', response_model=schemas.Token)
async def login(user_credentials: schemas.UserLogin):

    user = await models.UserModel.get(
        Q(email=user_credentials.email_username) |
        Q(username=user_credentials.email_username)
    )

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Credentials")

    access_token = oauth2.create_access_token(data={"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}

