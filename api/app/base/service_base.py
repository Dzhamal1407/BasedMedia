from typing import TypeVar, Type, Optional, List

from fastapi import HTTPException
from pydantic import BaseModel
from tortoise import models
from tortoise.contrib.pydantic import PydanticModel


ModelType = TypeVar("ModelType", bound=models.Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
GetSchemaType = TypeVar("GetSchemaType", bound=PydanticModel)
OutSchemaType = TypeVar("OutSchemaType", bound=PydanticModel)
QuerySchemaType = TypeVar("QuerySchemaType", bound=BaseModel)


class BaseService:
    model: Type[ModelType]
    create_schema: CreateSchemaType
    update_schema: UpdateSchemaType
    query_schema: QuerySchemaType
    get_schema: GetSchemaType
    out_schema: OutSchemaType

    async def create(self, schema: CreateSchemaType, **kwargs) -> Optional[GetSchemaType]:
        """CREATES AN OBJECT WITH OPTIONAL PARAMS"""
        obj = await self.model.create(**schema.dict(exclude_unset=True), **kwargs)
        return await self.get_schema.from_tortoise_orm(obj)

    async def all(self) -> Optional[List[GetSchemaType]]:
        """RETURNS ALL OBJECTS"""
        return await self.get_schema.from_queryset(self.model.all())

    async def get_obj(self, **kwargs) -> Optional[GetSchemaType]:
        """RETURNS ONE OBJECT"""
        return await self.model.get_or_none(**kwargs)

