from .BaseModel import *
from .CompanyModel import *
from include.dto.UserDTO import UserDTO


class IdCompanyRelationModel(BaseModel):
    id = PrimaryKeyField(null=False)
    id_company = IntegerField()
    id_api_company = IntegerField()

    @staticmethod
    def create_comp_relation(user_dto: UserDTO, company: CompanyModel):
        
        row = IdCompanyRelationModel(
            id_company = company.id,
            id_api_company = user_dto.comp_id,
        )
        row.save()

        return row

    class Meta():
        db_table = "id_company_relation"
        order_by = ('id',)