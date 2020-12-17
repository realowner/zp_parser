#!venv/bin/python3
from include.dto.UserDTO import UserDTO
from include.dto.VacancyDTO import VacancyDTO
from include.ArgsParse import ArgsParser
from include.api.ZarplataApi import ZpApi
from include.helpers.PhoneFormat import PhoneFormat
from include.helpers.PasswordGen import PasswordGen
import requests
from include.db import *
import json


def parser(args):
    skiped_comp_count = 0
    commited_comp = 0
    skiped_vac_count = 0
    commited_vac = 0
 
    try:
        company_id_list = [comp.company_id for comp in CompanyModel.select(CompanyModel.company_id)]
    except:
        print('Error occured when getting companies, falling back on empty list')
        company_id_list = []

    try:
        vacancy_id_list = [vac.vacancy_id for vac in VacancyModel.select(VacancyModel.vacancy_id)]
    except:
        print('Error occured when getting vacancies, falling back on empty list')
        company_id_list = []

    result = ''
    try:
        geo_count = api.do_geo_request(limit=0, offset=0, certain_id=args.geo_id)['metadata']['resultset']['count']
        for counter in range(0, geo_count, 100):
            geo_res = api.do_geo_request(limit=100, offset=counter, certain_id=args.geo_id)
            for geo_item in geo_res['geo']:
                print(f"{geo_item['id']} - {geo_item['name']}")
                rubric_res = api.do_rubric_request(certain_id=args.rubric_id)['rubrics']
                for rubric in rubric_res:
                    print(f"{rubric['id']} - {rubric['title']}")                    
                    vacancy_count = api.do_vacancy_request(geo_id=geo_item['id'], rubric_id=rubric['id'], limit=0, offset=0)['metadata']['resultset']['count']
                    current_company_list = []
                    for counter in range(0, vacancy_count, 100):
                        vacancy_res = api.do_vacancy_request(geo_id=geo_item['id'], rubric_id=rubric['id'], limit=100, offset=counter)
                        with db_handle.atomic():
                            for vacancy in vacancy_res['vacancies']:
                                vacancy_dto = VacancyDTO(vacancy)
                                if vacancy_dto.owner not in current_company_list:
                                    
                                    if vacancy_dto.owner in company_id_list:
                                        skiped_comp_count += 1
                                    else:
                                        company_res = api.do_company_request(company_id=vacancy_dto.owner)
                                        user_dto = UserDTO(company_res['companies'][0])
                                        current_company_list.append(vacancy_dto.owner)
                                        user_insert = UserModel.crate_user(user_dto)
                                        employer_insert = EmployerModel.create_employer(user_insert, user_dto)
                                        company_insert = CompanyModel.create_company(user_insert, user_dto)
                                        phone_insert = PhoneModel.create_phone(user_dto.phone, user_insert, company_insert, employer_insert)
                                        commited_comp += 1

                                if vacancy_dto.vac_id in vacancy_id_list:
                                    skiped_vac_count += 1
                                else:
                                    vacancy_insert = VacancyModel.create_vacancy(vacancy_dto)
                                    commited_vac += 1

                            db_handle.commit()

                            print(f'{skiped_comp_count} companies skiped')
                            print(f'{skiped_vac_count} vacancies skiped')
                            print(f'{commited_vac} vacancies, {commited_comp} owners info commited\n')
        result = 'Completed successfully'
    except:
        result = '\nFailed'

    return result


if __name__ == '__main__':
    args = ArgsParser.parse()
    api = ZpApi()

    if args.geo_id and args.rubric_id:
        print(f'Parsing with GEO={args.geo_id}, RUBRIC={args.rubric_id}...\n')
        execution = parser(args)
        print(execution)
    elif args.geo_id or args.rubric_id:
        print("You'r trying run parser with one argument")
        confim = input('Are you sure? (y/anything):')
        if confim == 'y':
            print(f'Parsing with geo={args.geo_id}, rubric={args.rubric_id}...\n')            
            execution = parser(args)
            print(execution)
        else:
            print('Exit')        
    else:
        print("You'r trying run parser without arguments")
        confim = input('Are you sure? (y/anything):')
        if confim == 'y':
            print(f'Parsing with geo={args.geo_id}, rubric={args.rubric_id}...\n')            
            execution = parser(args)
            print(execution)
        else:
            print('Exit')
