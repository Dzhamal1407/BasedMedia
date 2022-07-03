from tortoise import fields, models, Tortoise
from api.app.user.models import UserModel


class Post(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(null=False, max_length=255)
    content = fields.TextField(null=False)
    host: fields.ForeignKeyRelation['UserModel'] = fields.ForeignKeyField(
        'models.UserModel', related_name='posts', on_delete=fields.SET_NULL, null=True
    )


Tortoise.init_models(['api.app.content.models'], 'models')
