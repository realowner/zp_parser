from .BaseModel import *
from .VacancyModel import *
from include.dto.VacancyDTO import VacancyDTO


class IdVacancyRelationModel(BaseModel):
    id = PrimaryKeyField(null=False)
    id_vacancy = IntegerField()
    id_api_vacancy = IntegerField()

    @staticmethod
    def create_vac_relation(vacancy_dto: VacancyDTO, vacancy: VacancyModel):
        
        row = IdVacancyRelationModel(
            id_vacancy = vacancy.id,
            id_api_vacancy = vacancy_dto.vac_id,
        )
        row.save()

        return row

    class Meta():
        db_table = "id_vacancy_relation"
        order_by = ('id',)