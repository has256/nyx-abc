import lxml.html
import requests


class SummaryClient():

    LOGIN_URL = 'https://matricula.ufabc.edu.br/login/logar'
    SUMMARY_URL = 'https://matricula.ufabc.edu.br/matricula/resumo'

    @classmethod
    def get_my_subjects(cls, username, password):

        payload = f'uid={username}&senha={password}&commit=Entrar'

        response = requests.request(
            "POST",
            cls.LOGIN_URL,
            data=payload
        )

        headers = {
            "Cookie": f'_matricula_session={response.cookies["_matricula_session"]};',
        }

        response = requests.request(
            "GET",
            cls.SUMMARY_URL,
            headers=headers,
            cookies=response.cookies
        )

        page = lxml.html.fromstring(response.text)

        subjects = list(filter(lambda x: x != '', map(lambda x: x.strip().replace('\\n', ''),
                                                      page.xpath("//fieldset/ul/li/text()"))))

        schedule = list(filter(lambda x: x != [], [
            page.xpath(f"//fieldset/ul/li[{i}]/ul/li/text()") for i in range(len(subjects) + 1)
        ]))

        subjects_with_schedule = list(zip(subjects, schedule))

        return subjects_with_schedule
