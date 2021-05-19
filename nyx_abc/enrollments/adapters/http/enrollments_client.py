import requests
import json


class EnrollmentsClient():

    API_BASE_URL = 'https://matricula.ufabc.edu.br/cache/contagemMatriculas.js'

    @classmethod
    def get_enrollments_counter(cls):

        response = requests.get(
            cls.API_BASE_URL
        )

        enrollments_counter = response.content.decode("utf-8")[19:-2]

        if response.status_code == 200:
            return {
                'status_code': 200,
                'body': json.loads(enrollments_counter)
            }
