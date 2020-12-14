#!venv/bin/python3
from include.dto.UserDTO import UserDTO
from include.dto.VacancyDTO import VacancyDTO
from include.ArgsParse import ArgsParser
from include.api.ZarplataApi import ZpApi
from include.helpers.PhoneFormat import PhoneFormat
from include.helpers.PasswordGen import PasswordGen
import requests
# from include.db import *
import json

if __name__ == '__main__':
    args = ArgsParser.parse()
    api = ZpApi()

    vacancy_count = api.do_vacancy_request(geo_id=61, rubric_id=20, limit=0, offset=0)['metadata']['resultset']['count']
    company_list = []
    for counter in range(0, vacancy_count, 100):
        vacancy_res = api.do_vacancy_request(geo_id=61, rubric_id=20, limit=100, offset=counter)
        for vacancy in vacancy_res['vacancies']:
            vacancy_dto = VacancyDTO(vacancy)
            # point = 'test'
            if vacancy_dto.owner not in company_list:
                company_res = api.do_company_request(company_id=vacancy_dto.owner)
                user_dto = UserDTO(company_res['companies'][0])
                company_list.append(vacancy_dto.owner)
            
            

    point = 'test'



    # vacancy_dto = VacancyDTO(res['vacancies'][0])
    # user_dto = UserDTO(res['companies'][0])

    # user = UserModel.crate_user(user_dto)

    # employer = EmployerModel.create_employer(user, user_dto)

    # company = CompanyModel.create_company(user, user_dto)

    # phone = PhoneModel.create_phone(user_dto.phone, user, company)


    # print(f'{args.base_region_url}')
