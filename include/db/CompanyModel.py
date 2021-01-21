from .BaseModel import *
from .UserModel import *
from .EmployerModel import *
from include.dto.UserDTO import UserDTO


class CompanyModel(BaseModel):
    id = PrimaryKeyField(null=False)
    user_id = IntegerField()
    name = CharField(max_length=255)
    image_url = CharField(max_length=255)
    website = CharField(max_length=255)
    activity_field = TextField()
    vk = CharField(max_length=255)
    facebook = CharField(max_length=255)
    instagram = CharField(max_length=255)
    skype = CharField(max_length=255)
    description = TextField()
    contact_person = CharField(max_length=255)
    status = IntegerField(default=1)
    created_at = IntegerField()
    updated_at = IntegerField()
    owner = IntegerField()
    is_trusted = IntegerField(default=0)
    balance = DecimalField(max_digits=10, decimal_places=2, default=0.00)
    vacancy_renew_count = IntegerField(default=1)
    create_vacancy = IntegerField(default=3)

    @staticmethod
    def create_company(user: UserModel, user_dto: UserDTO, employer: EmployerModel):
        # exists = CompanyModel.get_or_none(CompanyModel.user_id == user_model.id)

        # if not bool(exists):
        row = CompanyModel(
            user_id = user.id,
            name = user_dto.title,
            image_url = user_dto.logo,
            website = user_dto.website,
            activity_field = user_dto.activity_field,
            vk = user_dto.vk,
            facebook = user_dto.facebook,
            instagram = user_dto.instagram,
            skype = user_dto.skype,
            description = user_dto.description,
            
            created_at = user_dto.created_at,
            updated_at = user_dto.updated_at,
            owner = user.id,
        )

        buffer = []
        if user_dto.firstname:
            buffer.append(user_dto.firstname)
        if user_dto.lastname:
            buffer.append(user_dto.lastname)
        row.contact_person = ' '.join(buffer)

        row.save()

        return row

        # return exists

    class Meta:
        db_table = "company"
        order_by = ('created_at',)
