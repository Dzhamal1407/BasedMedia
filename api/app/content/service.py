from ..base.service_base import BaseService
from fastapi import UploadFile
from . import schemas, models
import os
import uuid
import cv2
import json


class FileService:

    @staticmethod
    async def create_file(file: UploadFile) -> str:
        file_extension = file.filename.split('.').pop()
        file_name = str(uuid.uuid4()) + '.' + file_extension
        file_path = os.getcwd() + "/api/static/" + file_name
        contents = await file.read()
        with open(file_path, 'wb+') as f:
            f.write(contents)
            f.close()
        img = cv2.imread(file_path, 0)
        height, width = img.shape[:2]
        dictionary = {
            "file": file_name,
            "height": height,
            "width": width,
        }
        return json.dumps(dictionary)

    @staticmethod
    async def delete_file(filepath: str) -> str:
        os.remove("/api/static/"+filepath)


class PostService(BaseService):
    model = models.Post
    create_schema = schemas.PostCreate
    get_schema = schemas.PostGet

    async def create_post(self, schema: schemas.PostCreate, **kwargs):
        if schema.image:

            schema.image = await FileService.create_file(schema.image)

        post = await self.model.create(**schema.dict(exclude_unset=True), **kwargs)
        return await self.get_schema.from_tortoise_orm(post)


post_s = PostService()
