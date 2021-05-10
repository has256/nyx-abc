import requests
import json


class SigaaClient():

    API_BASE_URL = 'https://sig.ufabc.edu.br/sigaa/APISistemasNTI'

    @classmethod
    def get_infos_by_user(cls, user):

        response = requests.get(
            f'{cls.API_BASE_URL}?funcao=2&valor={user}'
        )

        if response.status_code == 200:
            return {
                'status_code': 200,
                'body': response.json()
            }
        else:
            return {
                'status_code': response.status_code,
                'body': response.json()
            }
