from include.helpers.PasswordGen import PasswordGen as pw
import time


class UserDTO:
    def __init__(self, user):
        dt: int = int(round(time.time()))
        self.email = user.get('email', 'some@mail.ru')
        self.title = user.get('title', 'Имя компании')
        self.website = user.get('external_url', '')
        self.username = user.get('email', 'some@mail.ru')
        self.description = user.get('description', 'Описание')
        self.password_hash = pw.password_hash(pw.generate_str())
        self.auth_key = pw.generate_str(32)
        self.confirmed_at = dt
        self.created_at = dt
        self.updated_at = dt

        self.firstname = ''
        self.lastname = ''
        self.logo = ''
        self.activity_field = ''

        if any([item for item in user.get('contacts', [])]):
            self.firstname = user['contacts'][0].get('firstname', '')
            self.lastname = user['contacts'][0].get('lastname', '')
            phones = user['contacts'][0].get('phones', [])
            if any([item for item in phones]):
                self.phone = phones[0].get('phone', None)

        if any([item for item in user.get('logo', [])]):
            self.logo = user['logo'].get('url')

        if any([item for item in user.get('rubrics', [])]):
            for rubric in user.get('rubrics'):
                self.activity_field = self.activity_field + rubric.get('title', '') + ' '
