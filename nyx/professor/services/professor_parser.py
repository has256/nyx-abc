import click
from nyx.professor.models.professor_model import Professor


class ProfessorParser():

    @classmethod
    def parse(cls, response):
        professor = Professor(response["siape"],
                              response["nome"], response["unidade_exercicio"])
        click.echo(professor)
