import lxml.html
import json
import requests
import unidecode


class UfabcClient():

    BASE_URL = 'https://www.ufabc.edu.br/ensino/docentes'

    @classmethod
    def get_research_area(cls, professor=None, area=None):

        response = requests.get(
            f'{cls.BASE_URL}'
        ).content

        if professor:
            page = lxml.html.fromstring(response)
            research_area = page.xpath(
                f"//td[contains(@data-order, '{format_name(professor)}')]/following-sibling::td[1]/small/text()"
            )[0]
            return research_area


def format_name(name):
    return unidecode.unidecode(' '.join(list(map(str.capitalize, name.lower().split(' ')))))
