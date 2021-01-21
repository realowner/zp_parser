import time
from include.helpers.Conformity import Conformity as conf


class VacancyDTO:

    def __init__(self, vacancy):
        dt: int = int(round(time.time()))

        # vacancy id for list only
        self.vac_id = vacancy['id']

        self.post = vacancy.get('header', 'Title')
        self.responsibilities = None
        self.min_salary = vacancy.get('salary_min', 0)
        self.max_salary = vacancy.get('salary_max', 0)
        self.qualification_requirements = None
        
        try:
            self.work_experience = conf.work_experience(self, received_id=vacancy['experience_length']['id'])
        except:
            self.work_experience = None
        
        try:
            self.education = vacancy['education']['title']
        except:
            self.education = None

        self.working_conditions = ''
        if any([item for item in vacancy.get('benefits', [])]):
            for benefit in vacancy['benefits']:
                self.working_conditions = self.working_conditions + benefit['title'] + '; '

        self.video = None
        self.city_id = vacancy['contact']['city']['id']
        self.address = vacancy['contact']['address']
        self.home_number = vacancy['contact']['building']
        
        try:
            if vacancy['schedule'] and vacancy['schedule']['id'] == 306:
                self.employment_type_id = 1
            else:
                self.employment_type_id = conf.employment_type(self, received_id=vacancy['working_type']['id'])
        except:
            self.employment_type_id = None

        self.hot = None
        self.notification_status = None
        self.status = None
        self.created_at = dt
        self.updated_at = dt
        
        # company id for list only
        self.company_id = vacancy['publication']['company_id']

        self.update_time = dt
        self.description = vacancy['description']        
        self.get_update_id = None
        self.views = None
        self.phone = vacancy['contact']['phones']
        self.active_until = None
        self.day_vacancy_untl = None

        self.main_categories = ''
        if any([item for item in vacancy.get('rubrics', [])]):
            for rubric in vacancy['rubrics']:
                self.main_categories = self.main_categories + rubric['title'] + '; '

