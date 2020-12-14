from .BaseModel import *
from .UserModel import *
from include.dto.UserDTO import UserDTO


class CompanyModel(BaseModel):
    id = PrimaryKeyField(null=False)
    user_id = IntegerField()
    name = CharField(max_length=255)
    image_url = CharField(max_length=255)
    website = CharField(max_length=255)
    activity_field = CharField(max_length=255)
    description = CharField()
    contact_person = CharField(max_length=255)
    status = IntegerField(default=1)
    created_at = IntegerField()
    updated_at = IntegerField()
    owner = IntegerField()

    @staticmethod
    def create_company(user_model: UserModel, user_dto: UserDTO):
        exists = CompanyModel.get_or_none(CompanyModel.user_id == user_model.id)

        if not bool(exists):
            row = CompanyModel(
                user_id=user_model.id,
                name=user_dto.title,
                image_url=user_dto.logo,
                website=user_dto.website,
                activity_field=user_dto.activity_field,
                description=user_dto.description,
                created_at=user_dto.created_at,
                updated_at=user_dto.updated_at,
                owner=user_model.id,
            )

            buffer = []
            if user_dto.firstname:
                buffer.append(user_dto.firstname)
            if user_dto.lastname:
                buffer.append(user_dto.lastname)
            row.contact_person = ' '.join(buffer)

            row.save()

            return row

        return exists

    class Meta:
        db_table = "company"
        order_by = ('created_at',)
