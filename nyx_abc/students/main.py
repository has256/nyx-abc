from nyx_abc.students.adapters.http.client import SigaaClient
from nyx_abc.students.services.student_parser import StudentParser
import click


@click.group('aluno')
def aluno():
    """Utilitarios de Alunos(as)"""
    ...


@aluno.command()
@click.argument('arg')
def info(arg):
    """Retorna infos completas usando RA, usuario ou email como argumento"""

    response = SigaaClient.get_infos_by_user(arg)

    if response["status_code"] == 200:
        StudentParser.parse(response['body'])
    else:
        click.echo(response["body"])
