from peewee import *
from .BaseModel import *
from .CompanyModel import *
from include.dto.VacancyDTO import VacancyDTO


class VacancyModel(BaseModel):
    id = PrimaryKeyField(null=False)

    company_id = IntegerField

    post = CharField(max_length=255)
    responsibilities = TextField
    min_salary = IntegerField()
    max_salary = IntegerField()
    qualification_requirements = TextField
    work_experence = CharField(max_length=255)
    education = CharField(max_length=255)
    work_conditions = TextField
    video = CharField(max_length=255)
    city_id = IntegerField()

    address = CharField(max_length=255)
    home_number = CharField(max_length=255)

    employment_type_id = IntegerField()
    hot = IntegerField(default=0)
    notification_status = IntegerField(default=0)
    status = IntegerField(default=1)
    created_at = IntegerField()
    updated_at = IntegerField()
    owner = IntegerField()
    updated_time = IntegerField()
    description = TextField

    main_category_id = IntegerField(default=34)

    publisher_id = IntegerField
    get_update_id = IntegerField(default=0)
    views = IntegerField(default=0)
    phone = CharField(max_length=255)
    active_until = CharField(max_length=255)
    day_vacancy_until = IntegerField(default=0)
    # main_categories = CharField(max_length=255)



    @staticmethod
    def create_vacancy(vacancy_dto: VacancyDTO, company: CompanyModel):
        """
        :param user_dto: UserDTO
        :return: UserModel
        """
        # exists = UserModel.get_or_none(UserModel.email == user_dto.email)

        # if not bool(exists):

        row = VacancyModel(
            company_id = company.id,
            post = vacancy_dto.post,
            responsibilities = vacancy_dto.responsibilities,
            min_salary = vacancy_dto.min_salary,
            max_salary = vacancy_dto.max_salary,
            qualification_requirements = vacancy_dto.qualification_requirements,
            work_experence = vacancy_dto.work_experence,
            education = vacancy_dto.education,
            work_conditions = vacancy_dto.work_conditions,
            video = vacancy_dto.video,
            city_id = vacancy_dto.city_id,
            # address ???
            # home_number ???
            employment_type_id = vacancy_dto.employment_type,
            created_at = vacancy_dto.created_at,
            updated_at = vacancy_dto.updated_at,
            owner = vacancy_dto.owner,
            updated_time = vacancy_dto.update_time,
            description = vacancy_dto.description,
            # main_category_id ???
            publisher_id = vacancy_dto.publisher_id,
            phone = vacancy_dto.phone,
            active_until = vacancy_dto.active_until,
            # main_categories = vacancy_dto.main_categories,
        )
        row.save()

        return row

        # return exists

    class Meta:
        db_table = "vacancy"
        order_by = ('created_at',)