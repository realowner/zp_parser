from .BaseModel import *
from .UserModel import *
from .CompanyModel import *
from .EmployerModel import *
from include.helpers.PhoneFormat import PhoneFormat


class PhoneModel(BaseModel):
    id = PrimaryKeyField(null=False)
    company_id = IntegerField()
    employer_id = IntegerField()
    number = CharField(max_length=255)
    owner = IntegerField()

    @staticmethod
    def create_phone(phone: str, user: UserModel, company: CompanyModel, employer: EmployerModel):
        phone_format = PhoneFormat(phone=phone, tpl='+$ $$$ $$$-$$-$$')
        row = PhoneModel(
            company_id=company.id,
            employer_id=employer.id,
            number=phone_format.phone,
            owner=user.id
        )

        row.save()

        return row

    class Meta:
        db_table = "phone"
        order_by = ('id',)
