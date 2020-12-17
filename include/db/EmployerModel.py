from .BaseModel import *
from .UserModel import *
from include.dto.UserDTO import UserDTO


class EmployerModel(BaseModel):
    id = PrimaryKeyField(null=False)
    user_id = IntegerField()
    first_name = CharField(max_length=255)
    second_name = CharField(max_length=255)
    status = IntegerField(default=1)
    created_at = IntegerField()
    updated_at = IntegerField()
    owner = IntegerField()
    audit_count = IntegerField(default=0)

    @staticmethod
    def create_employer(user_model: UserModel, user_dto: UserDTO):
        # exists = EmployerModel.get_or_none(EmployerModel.user_id == user_model.id)

        # if not bool(exists):
        row = EmployerModel(
            user_id=user_model.id,
            first_name=user_dto.firstname,
            second_name=user_dto.lastname,
            created_at=user_dto.created_at,
            updated_at=user_dto.updated_at,
            owner=user_model.id,
        )
        row.save()

        return row

        # return exists

    class Meta:
        db_table = "employers"
        order_by = ('created_at',)
