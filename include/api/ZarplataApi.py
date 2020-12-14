import requests
import json

class ZpApi:

    def __init__(self):
        self.type = None
        # self.base_region_url = base_region_url
        self.id = None
        self.headers = {
            #TODO: add headers from dev panel
        }
        self.cookies = {
            # key - proxy
            # value - proxy' cookies
        }

    # def do_request(self, obj_type, obj_id=None, additional_params=None):
    #     url = f'https://{self.base_region_url}.zarplata.ru/api/v1/{obj_type}'
    #     if obj_id:
    #         url = f'{url}/{obj_id}'

    #     if additional_params:
    #         url = f'{url}/?{additional_params}'

    #     response = requests.get(url)
    #     if response.status_code == 200:
    #         return json.loads(response.text)

    #     return None

    def do_request(self, url):

        response = requests.get(url)
        if response.status_code == 200:
            return json.loads(response.text)

    def do_vacancy_request(self, geo_id, rubric_id, limit, offset):
        url = f'https://zarplata.ru/api/v1/vacancies?geo_id={geo_id}&rubric_id[]={rubric_id}&limit={limit}&offset={offset}'
        return self.do_request(url=url)


    def do_company_request(self, company_id):
        url = f'https://zarplata.ru/api/v1/companies/{company_id}'
        return self.do_request(url=url)


    def do_rubric_request(self):
        url = 'https://zarplata.ru/api/v1/rubrics'
        return self.do_request(url)



