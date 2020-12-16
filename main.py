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

if __name__ == '__main__':
    args = ArgsParser.parse()
    api = ZpApi()


    # geo_count = api.do_geo_request(limit=0, offset=0)['metadata']['resultset']['count']
    # for counter in range(0, geo_count, 100):
    #     geo_res = api.do_geo_request(limit=100, offset=counter)
    #     for geo_item in geo_res['geo']:
    #         rubric_res = api.do_rubric_request()['rubrics']
    #         for rubric in rubric_res:
    #             vacancy_count = api.do_vacancy_request(geo_id=geo_item['id'], rubric_id=rubric['id'], limit=0, offset=0)['metadata']['resultset']['count']
    #             company_list = []
    #             for counter in range(0, vacancy_count, 100):
    #                 vacancy_res = api.do_vacancy_request(geo_id=geo_item['id'], rubric_id=rubric['id'], limit=100, offset=counter)
    #                 for vacancy in vacancy_res['vacancies']:
    #                     vacancy_dto = VacancyDTO(vacancy)
    #                     if vacancy_dto.owner not in company_list:
    #                         company_res = api.do_company_request(company_id=vacancy_dto.owner)
    #                         user_dto = UserDTO(company_res['companies'][0])
    #                         company_list.append(vacancy_dto.owner)
    #                         company_list.append(vacancy_dto.owner)
    #                         user_insert = UserModel.crate_user(user_dto)
    #                         employer_insert = EmployerModel.create_employer(user_insert, user_dto)
    #                         company_insert = CompanyModel.create_company(user_insert, user_dto)
    #                         phone_insert = PhoneModel.create_phone(user_dto.phone, user_insert, company_insert, employer_insert)
    #                     vacancy_insert = VacancyModel.create_vacancy(vacancy_dto)

    #TODO: add proxies, args
    
    vacancy_count = api.do_vacancy_request(geo_id=61, rubric_id=138, limit=0, offset=0)['metadata']['resultset']['count']
    company_list = []
    for counter in range(0, vacancy_count, 100):
        vacancy_res = api.do_vacancy_request(geo_id=61, rubric_id=138, limit=100, offset=counter)
        with db_handle.atomic():
            for vacancy in vacancy_res['vacancies']:
                vacancy_dto = VacancyDTO(vacancy)
                if vacancy_dto.owner not in company_list:
                    company_res = api.do_company_request(company_id=vacancy_dto.owner)
                    user_dto = UserDTO(company_res['companies'][0])
                    company_list.append(vacancy_dto.owner)
                    user_insert = UserModel.crate_user(user_dto)
                    employer_insert = EmployerModel.create_employer(user_insert, user_dto)
                    company_insert = CompanyModel.create_company(user_insert, user_dto)
                    phone_insert = PhoneModel.create_phone(user_dto.phone, user_insert, company_insert, employer_insert)
                vacancy_insert = VacancyModel.create_vacancy(vacancy_dto)
            db_handle.commit()
            
            

    point = 'test'



    # vacancy_dto = VacancyDTO(res['vacancies'][0])
    # user_dto = UserDTO(res['companies'][0])

    # user = UserModel.crate_user(user_dto)

    # employer = EmployerModel.create_employer(user, user_dto)

    # company = CompanyModel.create_company(user, user_dto)

    # phone = PhoneModel.create_phone(user_dto.phone, user, company)


    # print(f'{args.base_region_url}')
