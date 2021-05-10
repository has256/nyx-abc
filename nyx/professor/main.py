from nyx.professor.adapter.http.client import SigaaClient
from nyx.professor.service.professor_parser import ProfessorParser
import click


@click.group('docente')
def docente():
    """Utilitarios de Docentes"""
    ...


@docente.command()
@click.argument('arg')
def info(arg):
    """Retorna infos completas usando RA, usuario ou email como argumento"""

    response = SigaaClient.get_infos_by_user(arg)

    if response["status_code"] == 200:
        ProfessorParser.parse(response['body'])
    else:
        click.echo(response["body"])
