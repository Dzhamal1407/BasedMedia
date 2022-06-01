from tortoise import fields, models


class UserModel(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(null=False, max_length=20, unique=True)
    email = fields.CharField(null=False, max_length=255, unique=True)
    password = fields.CharField(null=False, max_length=255)
    joined = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table: str = 'users'


class Post(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(null=False, max_length=255)
    content = fields.TextField(null=False)
    host: fields.ForeignKeyRelation['UserModel'] = fields.ForeignKeyField(
        'models.UserModel', related_name='posts', on_delete=fields.SET_NULL, null=True
    )

