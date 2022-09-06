import os


DATABASE_URL = "postgres://dzham@localhost:5432/media"

APPS_MODELS = [
    "api.app.user.models",
    # "api.app.auth.models",
    "api.app.content.models",
]
