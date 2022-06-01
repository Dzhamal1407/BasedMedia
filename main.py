from fastapi import FastAPI
from api import auth, user
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

app.include_router(auth.auth_router)
app.include_router(user.user_router)


register_tortoise(
    app,
    db_url="postgres://postgres:topscr1407@localhost:5432/media",
    modules={"models": ["api.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
