from peewee import *
from .BaseModel import *
from include.dto.UserDTO import UserDTO


class UserModel(BaseModel):
    id = PrimaryKeyField(null=False)
    email = CharField(null=False, max_length=255)
    username = CharField(null=False, max_length=255)
    password_hash = CharField(null=False, max_length=60)
    auth_key = CharField(null=False, max_length=32)
    confirmed_at = IntegerField()
    unconfirmed_email = CharField(max_length=255)
    blocked_at = IntegerField()
    registration_ip = IntegerField()
    created_at = IntegerField()
    updated_at = IntegerField()
    flags = IntegerField(default=0)
    last_login_at = IntegerField()
    status = IntegerField()
    is_parsed = BooleanField(null=False, default=False)
    fake_email = BooleanField(null=False, default=False)

    @staticmethod
    def crate_user(user_dto: UserDTO, email=True):
        """
        :param user_dto: UserDTO
        :return: UserModel
        """
        # exists = UserModel.get_or_none(UserModel.email == user_dto.email)

        # if not bool(exists):
        if email == True:
            row = UserModel(
                email=user_dto.email,
                username=user_dto.email,
                password_hash=user_dto.password_hash,
                auth_key=user_dto.auth_key,
                confirmed_at=user_dto.confirmed_at,
                # unconfirmed_email ???
                # blocked_at ???
                # registration_ip ???
                created_at=user_dto.created_at,
                updated_at=user_dto.updated_at,
                # last_login_at ???
                # status ???
                is_parsed = True,
            )
        else:
            row = UserModel(
                email=user_dto.email,
                username=user_dto.email,
                password_hash=user_dto.password_hash,
                auth_key=user_dto.auth_key,
                confirmed_at=user_dto.confirmed_at,
                # unconfirmed_email ???
                # blocked_at ???
                # registration_ip ???
                created_at=user_dto.created_at,
                updated_at=user_dto.updated_at,
                # last_login_at ???
                # status ???
                is_parsed = True,
                fake_email = True,
            )

            
        row.save()

        return row

        # return exists

    class Meta:
        db_table = "user"
        order_by = ('created_at',)