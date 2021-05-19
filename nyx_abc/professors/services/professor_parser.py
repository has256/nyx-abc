import click
from nyx_abc.professors.models.professor_model import Professor


class ProfessorParser():

    @classmethod
    def parse(cls, response):
        professor = Professor(response["siape"],
                              response["nome"], response["unidade_exercicio"])
        click.echo(professor)

    @classmethod
    def parse_name(cls, response):
        professor = Professor(response["siape"],
                              response["nome"], response["unidade_exercicio"])
        return professor.name
