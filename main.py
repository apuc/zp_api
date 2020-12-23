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
    #res = requests.get('https://rostovskaya-oblast.zarplata.ru/api/v1/companies/18681793')
    # with open('./data_samples/beeline.json') as f:
    #     company = json.loads(f.read())

    api = ZpApi('rostovskaya-oblast')
    res = api.do_request('vacancies', 204506901)

    # hash = PasswordGen.password_hash('123edsaqw'.encode("utf-8"))
    # Some.test()
    # Some_2.my()

    # db = BaseModel()
    # print(123)
    vacancy_dto = VacancyDTO(res['vacancies'][0])
    user_dto = UserDTO(res['companies'][0])

    user = UserModel.crate_user(user_dto)

    employer = EmployerModel.create_employer(user, user_dto)

    company = CompanyModel.create_company(user, user_dto)

    phone = PhoneModel.create_phone(user_dto.phone, user, company)


    print(f'{args.base_region_url}')
