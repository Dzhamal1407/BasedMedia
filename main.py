from fastapi import FastAPI
from api.app.auth import auth
from api.app.user import user
from api.app.content import post
from api.config import settings
from fastapi.staticfiles import StaticFiles
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

app.include_router(auth.auth_router)
app.include_router(user.user_router)
app.include_router(post.post_router)

app.mount("/static", StaticFiles(directory="api/static"), name="static")

register_tortoise(
    app,
    db_url=settings.DATABASE_URL,
    modules={"models": settings.APPS_MODELS},
    generate_schemas=True,
    add_exception_handlers=True,
)
