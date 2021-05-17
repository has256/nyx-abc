import requests
import json


class SubjectsClient():

    API_BASE_URL = 'https://matricula.ufabc.edu.br/cache/todasDisciplinas.js'

    @classmethod
    def get_all_current_subjects(cls):

        response = requests.get(
            cls.API_BASE_URL
        )

        current_subjects = response.content.decode("utf-8")[17:-2]

        if response.status_code == 200:
            return {
                'status_code': 200,
                'body': json.loads(current_subjects)
            }
