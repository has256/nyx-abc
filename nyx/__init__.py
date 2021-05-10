from nyx.student.main import aluno
from nyx.professor.main import docente
from nyx.website.main import site
from nyx.disciplinas import disciplinas
from nyx.ementas import ementas
import click


@click.group('cli')
def cli():
    ...


cli.add_command(disciplinas)
cli.add_command(site)
cli.add_command(aluno)
cli.add_command(docente)
cli.add_command(ementas)

cli()
