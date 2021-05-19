from nyx_abc.professors.adapters.http.sigaa_client import SigaaClient
from nyx_abc.professors.adapters.http.ufabc_client import UfabcClient
from nyx_abc.professors.services.professor_parser import ProfessorParser
import click


@click.group('docente')
def docente():
    """Utilitarios de Docentes"""
    ...


@docente.command()
@click.argument('arg')
def info(arg):
    """Retorna infos completas usando SIAPE, usuario ou email como argumento"""

    response = SigaaClient.get_infos_by_user(arg)

    if response["status_code"] == 200:
        ProfessorParser.parse(response['body'])
    else:
        click.echo(response["body"])


@docente.command()
@click.argument('arg')
def area_de_pesquisa(arg):
    """Retorna infos completas usando RA, usuario ou email como argumento"""

    response = SigaaClient.get_infos_by_user(arg)

    if response["status_code"] == 200:
        professor_name = ProfessorParser.parse_name(response['body'])
        research_area = UfabcClient.get_research_area(professor=professor_name)
        click.echo(research_area)
    else:
        click.echo(response["body"])
