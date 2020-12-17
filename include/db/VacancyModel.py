from peewee import *
from .BaseModel import *
from include.dto.VacancyDTO import VacancyDTO


class VacancyModel(BaseModel):
    id = PrimaryKeyField(null=False)
    post = CharField(max_length=255)
    responsibilities = CharField(max_length=255)
    min_salary = IntegerField()
    max_salary = IntegerField()
    qualification_requirements = CharField(max_length=255)
    work_experence = CharField(max_length=255)
    education = CharField(max_length=255)
    work_conditions = CharField(max_length=255)
    video = CharField(max_length=255)
    city_id = CharField(max_length=255)
    employment_type_id = CharField(255)
    hot = IntegerField()
    notification_status = IntegerField()
    status = IntegerField()
    created_at = IntegerField()
    updated_at = IntegerField()
    owner = IntegerField()
    updated_time = IntegerField()
    description = CharField()
    publisher_id = IntegerField()
    get_update_id = IntegerField()
    views = IntegerField()
    phone = CharField(max_length=255)
    active_until = CharField(max_length=255)
    day_vacancy_until = IntegerField()
    main_categories = CharField(max_length=255)
    vacancy_id = IntegerField()



    @staticmethod
    def create_vacancy(vacancy_dto: VacancyDTO):
        """
        :param user_dto: UserDTO
        :return: UserModel
        """
        # exists = UserModel.get_or_none(UserModel.email == user_dto.email)

        # if not bool(exists):

        row = VacancyModel(
            post = vacancy_dto.post,
            # responsibilities = vacancy_dto.responsibilities,
            min_salary = vacancy_dto.min_salary,
            max_salary = vacancy_dto.max_salary,
            # qualification_requirements = vacancy_dto.qualification_requirements,
            work_experence = vacancy_dto.work_experence,
            education = vacancy_dto.education,
            work_conditions = vacancy_dto.work_conditions,
            # video = vacancy_dto.video,
            city_id = vacancy_dto.city_id,
            employment_type_id = vacancy_dto.employment_type_id,
            # hot = vacancy_dto.hot,
            # notification_status = vacancy_dto.notification_status,
            # status = vacancy_dto.status,
            created_at = vacancy_dto.created_at,
            updated_at = vacancy_dto.updated_at,
            owner = vacancy_dto.owner,
            updated_time = vacancy_dto.update_time,
            description = vacancy_dto.description,
            publisher_id = vacancy_dto.publisher_id,
            # get_update_id = vacancy_dto.get_update_id,
            # views = vacancy_dto.views,
            phone = vacancy_dto.phone,
            active_until = vacancy_dto.active_until,
            # day_vacancy_until = vacancy_dto.day_vacancy_untl,
            main_categories = vacancy_dto.main_categories,
            vacancy_id = vacancy_dto.vac_id
        )
        row.save()

        return row

        # return exists

    class Meta:
        db_table = "vacancies"
        order_by = ('created_at',)