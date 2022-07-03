from ..base.service_base import BaseService
from . import schemas, models


class PostService(BaseService):
    model = models.Post
    create_schema = schemas.PostCreate
    get_schema = schemas.PostGet


post_s = PostService()
