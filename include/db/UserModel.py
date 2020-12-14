from peewee import *
from .BaseModel import *
from include.dto.UserDTO import UserDTO


class UserModel(BaseModel):
    id = PrimaryKeyField(null=False)
    email = CharField(max_length=255)
    username = CharField(max_length=255)
    password_hash = CharField(max_length=60)
    auth_key = CharField(max_length=32)
    confirmed_at = IntegerField()
    created_at = IntegerField()
    updated_at = IntegerField()

    @staticmethod
    def crate_user(user_dto: UserDTO):
        """
        :param user_dto: UserDTO
        :return: UserModel
        """
        exists = UserModel.get_or_none(UserModel.email == user_dto.email)

        if not bool(exists):
            row = UserModel(
                email=user_dto.email,
                username=user_dto.username,
                password_hash=user_dto.password_hash,
                auth_key=user_dto.auth_key,
                confirmed_at=user_dto.confirmed_at,
                created_at=user_dto.created_at,
                updated_at=user_dto.updated_at,
            )
            row.save()

            return row

        return exists

    class Meta:
        db_table = "user"
        order_by = ('created_at',)