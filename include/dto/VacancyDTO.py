import time


class VacancyDTO:

    def __init__(self, vacancy):
        dt: int = int(round(time.time()))

        #test only
        self.vac_id = vacancy['id']

        self.post = vacancy.get('header', 'Title')
        self.responsibilities = None
        self.min_salary = vacancy.get('salary_min', 0)
        self.max_salary = vacancy.get('salary_max', 0)
        self.qualification_requirements = None
        
        try:
            self.work_experence = vacancy['experience_length']['title']
        except:
            self.work_experence = None
        
        try:
            self.education = vacancy['education']['title']
        except:
            self.education = None

        self.work_conditions = ''
        if any([item for item in vacancy.get('benefits', [])]):
            for benefit in vacancy['benefits']:
                self.work_conditions = self.work_conditions + benefit['title'] + '; '

        self.video = None
        self.city_id = vacancy['contact']['city']['title']
        
        try:
            self.employment_type_id = vacancy['working_type']['title']
        except:
            self.employment_type_id = None

        self.hot = None
        self.notification_status = None
        self.status = None
        self.created_at = dt
        self.updated_at = dt
        
        # conmpany_id for FK
        self.owner = vacancy['publication']['company_id']

        self.update_time = dt
        self.description = vacancy['description']
        
        # conmpany_id for FK
        self.publisher_id = vacancy['publication']['company_id']
        
        self.get_update_id = None
        self.views = None
        self.phone = vacancy['contact']['phones']
        self.active_until = None
        self.day_vacancy_untl = None

        self.main_categories = ''
        if any([item for item in vacancy.get('rubrics', [])]):
            for rubric in vacancy['rubrics']:
                self.main_categories = self.main_categories + rubric['title'] + '; '

