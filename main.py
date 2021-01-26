#!venv/bin/python3
import logging
from re import T, U
from include.db.IdGeoRelationModel import IdGeoRelationModel
from include.dto.UserDTO import UserDTO
from include.dto.VacancyDTO import VacancyDTO
from include.ArgsParse import ArgsParser
from include.api.ZarplataApi import ZpApi
from include.helpers.EmailGenerator import EmailGenerator as emgen
from include.db import *
import time
import requests
import json

logging.basicConfig(filename='logs.log', filemode='w', level=logging.WARNING, format='%(name)s - %(levelname)s - %(message)s')

def parser(args):
    skiped_comp_count = 0
    commited_comp = 0
    skiped_vac_count = 0
    exist_vac_count = 0
    commited_vac = 0
    point = '--> '
 
    try:
        company_id_list = [comp.id_api_company for comp in IdCompanyRelationModel.select(IdCompanyRelationModel.id_api_company)]
    except:
        print('Error occured when getting companies, falling back on empty list')
        company_id_list = []
    try:
        vacancy_id_list = [vac.id_api_vacancy for vac in IdVacancyRelationModel.select(IdVacancyRelationModel.id_api_vacancy)]
    except:
        print('Error occured when getting vacancies, falling back on empty list')
        company_id_list = []

    result = ''
    try:
        geo_count = api.do_geo_request(limit=0, offset=0, certain_id=args.geo_id)['metadata']['resultset']['count']
        for counter in range(0, geo_count, 100):
            geo_res = api.do_geo_request(limit=100, offset=counter, certain_id=args.geo_id)
            for geo_item in geo_res['geo']:
                print("\n------------------------------------------------------")            
                print(f"    {geo_item['id']} - {geo_item['name']}")
                geo_db_matches = IdGeoRelationModel.get_or_none(IdGeoRelationModel.id_api_geo == geo_item['id'])
                if geo_db_matches == None:
                    print(point + 'no matches found in the database')
                    appropriate_geo_id = input(point + '    Enter the appropriate geo id: ')
                    appropriate_geo_id_fromdb = GeobaseModel.get(GeobaseModel.id == appropriate_geo_id)
                    print(point + f'        {appropriate_geo_id_fromdb.name}')
                    geo_rel_insert = IdGeoRelationModel.create_geo_relation(geo_item['id'], appropriate_geo_id, appropriate_geo_id_fromdb.name)
                    print(point + 'geo relation COMMITED')
                else:
                    geo_rel_insert = IdGeoRelationModel.get(IdGeoRelationModel.id_api_geo == geo_item['id'])
                    print(point + 'matches found in the database')
                    print(point + f'    {geo_db_matches.name}')
                rubric_res = api.do_rubric_request(certain_id=args.rubric_id)['rubrics']
                for rubric in rubric_res:
                    print(f"\n    {rubric['id']} - {rubric['title']}")
                    category_db_matches = IdCategoryRelationModel.get_or_none(IdCategoryRelationModel.id_api_category == rubric['id'])
                    if category_db_matches == None:
                        print(point + 'no matches found in the database')
                        appropriate_rubric_id = input(point + '    Enter the appropriate rubric id: ')
                        appropriate_rubric_id_fromdb = CategoryModel.get(CategoryModel.id == appropriate_rubric_id)
                        print(point + f'        {appropriate_rubric_id_fromdb.name}')
                        category_rel_insert = IdCategoryRelationModel.create_category_relation(rubric['id'], appropriate_rubric_id, appropriate_rubric_id_fromdb.name)
                        print(point + 'category relation COMMITED')
                    else:
                        category_rel_insert = IdCategoryRelationModel.get(IdCategoryRelationModel.id_api_category == rubric['id'])
                        print(point + 'matches found in the database')
                        print(point + f'    {category_db_matches.name}')
                        
                    print("------------------------------------------------------")                    
                    vacancy_count = api.do_vacancy_request(geo_id=geo_item['id'], rubric_id=rubric['id'], limit=0, offset=0)['metadata']['resultset']['count']
                    current_company_list = []
                    for counter in range(0, vacancy_count, 100):
                        vacancy_res = api.do_vacancy_request(geo_id=geo_item['id'], rubric_id=rubric['id'], limit=100, offset=counter)
                        with db_handle.atomic():
                            for vacancy in vacancy_res['vacancies']:
                                if vacancy['publication'] is not None and vacancy['publication']['company_id'] is not None:
                                    vacancy_dto = VacancyDTO(vacancy)
                                    simple_request = api.do_company_request(company_id=vacancy_dto.company_id)
                                    try:
                                        owner_email = simple_request['companies'][0]['email']
                                    except:
                                        owner_email = None
                                    print(f'\nvacancy {vacancy_dto.vac_id} company {vacancy_dto.company_id}({owner_email}):')

                                    if vacancy_dto.company_id not in current_company_list:
                                            
                                        if vacancy_dto.company_id in company_id_list:
                                            print(point + f'owners info {vacancy_dto.company_id}: already exist SKIPPED')
                                            skiped_comp_count += 1
                                            company_insert = CompanyModel.select().join(IdCompanyRelationModel).where(
                                                    IdCompanyRelationModel.id_api_company == vacancy_dto.company_id).get()
                                            if owner_email == None or owner_email == '':
                                                user_insert = UserModel.get(UserModel.email == emgen.email_generator(
                                                    simple_request['companies'][0]['title']))
                                            else:
                                                user_insert = UserModel.get(UserModel.email == owner_email)
                                        else:
                                            user_matches = UserModel.get_or_none(UserModel.email == owner_email)
                                            if user_matches == None:                                          
                                                company_res = api.do_company_request(company_id=vacancy_dto.company_id)
                                                user_dto = UserDTO(company_res['companies'][0])
                                                current_company_list.append(vacancy_dto.company_id)                                            
                                                if owner_email == None or owner_email == '':
                                                    print(point + f'owners info {vacancy_dto.company_id}: email does not exist')
                                                    user_insert = UserModel.crate_user(user_dto, email=False)
                                                    print(point + f'owners info {vacancy_dto.company_id}: email generated ({user_dto.email})')
                                                else:
                                                    print(point + f'owners info {vacancy_dto.company_id}: email exist')
                                                    user_insert = UserModel.crate_user(user_dto)
                                                print(point + 'user insert: done')
                                                employer_insert = EmployerModel.create_employer(user_insert, user_dto)
                                                print(point + 'employer insert: done')
                                                company_insert = CompanyModel.create_company(user_insert, user_dto, employer_insert)
                                                print(point + 'company insert: done')
                                                comp_rel_insert = IdCompanyRelationModel.create_comp_relation(user_dto, company_insert)
                                                print(point + 'company relation insert: done')
                                                phone_insert = PhoneModel.create_phone(user_dto.phone, user_insert, company_insert, employer_insert)
                                                print(point + 'phone insert: done')
                                                commited_comp += 1
                                                print(point + f'owners info {vacancy_dto.company_id}: SAVED')
                                            else:
                                                skiped_comp_count += 1
                                                company_insert = CompanyModel.select().join(IdCompanyRelationModel).where(
                                                        IdCompanyRelationModel.id_api_company == vacancy_dto.company_id)
                                                mail = api.do_company_request(company_id=vacancy_dto.company_id)
                                                user_insert = UserModel.get(UserModel.email == mail['companies'][0]['email'])
                                                print(point + f'owners info {vacancy_dto.company_id}: already exist SKIPPED')
                                    else:
                                        print(point + f'owners info {vacancy_dto.company_id}: already exist SKIPPED (current)')

                                    if vacancy_dto.vac_id in vacancy_id_list:
                                        exist_vac_count += 1
                                        print(point + f'vacancy {vacancy_dto.vac_id}: already exist SKIPPED')
                                    else:
                                        try:
                                            vacancy_insert = VacancyModel.create_vacancy(vacancy_dto, company_insert, user_insert, category_rel_insert, geo_rel_insert)
                                            print(point + f'vacancy insert: done')
                                            vac_rel_insert = IdVacancyRelationModel.create_vac_relation(vacancy_dto, vacancy_insert)
                                            print(point + f'vacancy relation insert: done')
                                            commited_vac += 1                                
                                            print(point + f'vacancy {vacancy_dto.vac_id}: SAVED')
                                        except:
                                            skiped_vac_count += 1
                                            print(point + f'vacancy {vacancy_dto.vac_id}: insert failed SKIPPED')
                                else:
                                    print(f'\nvacancy {vacancy_dto.vac_id}: company does not exist SKIPPED')
                                    skiped_vac_count += 1

                            db_handle.commit()

            print(f'\nTotal number of vacancies: {vacancy_count}')
            print(f'{exist_vac_count} vacancies already exist SKIPPED')
            print(f'{skiped_vac_count} vacancies SKIPPED')
            print(f'{skiped_comp_count} owners info SKIPPED')
            print(f'{commited_vac} vacancies, {commited_comp} owners info COMMITED')

            result = '\nCompleted successfully'
    except Exception:
        logging.exception(msg="Attention!")
        result = '\nFailed'

    return result

if __name__ == '__main__':
    args = ArgsParser.parse()
    api = ZpApi()

    if args.geo_id and args.rubric_id:
        print(f'Parsing with GEO={args.geo_id}, RUBRIC={args.rubric_id}...')
        confim = input("Continue? (y/anything):")
        if confim == 'y':
            start_time = time.time()
            execution = parser(args)
            print(execution)
            print(f'Working time: {time.time() - start_time} seconds')
        else:
            print('Bye')
    elif args.geo_id or args.rubric_id:
        print(f'Parsing with GEO={args.geo_id}, RUBRIC={args.rubric_id}...\n')
        print("You'r trying run parser with one argument")
        confim = input('Are you sure? (y/anything):')
        if confim == 'y':
            start_time = time.time()
            print(f'Parsing with geo={args.geo_id}, rubric={args.rubric_id}...\n')            
            execution = parser(args)
            print(execution)
            print(f'Working time: {time.time() - start_time} seconds')
        else:
            print('Bye')        
    else:
        print("You'r trying run parser without arguments")
        confim = input('Are you sure? (y/anything):')
        if confim == 'y':
            start_time = time.time()
            print(f'Parsing with geo={args.geo_id}, rubric={args.rubric_id}...\n')            
            execution = parser(args)
            print(execution)
            print(f'Working time: {time.time() - start_time} seconds')
        else:
            print('Bye')
