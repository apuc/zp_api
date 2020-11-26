import requests
import json

class ZpApi:

    def __init__(self, base_region_url):
        self.type = None
        self.base_region_url = base_region_url
        self.id = None
        self.headers = {
            #TODO: add headers from dev panel
        }
        self.cookies = {
            # key - proxy
            # value - proxy' cookies
        }

    def do_request(self, obj_type, obj_id=None, additional_params=None):
        url = f'https://{self.base_region_url}.zarplata.ru/api/v1/{obj_type}'
        if obj_id:
            url = f'{url}/{obj_id}'

        if additional_params:
            url = f'{url}/?{additional_params}'

        response = requests.get(url)
        if response.status_code == 200:
            return json.loads(response.text)

        return None
