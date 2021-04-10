from .disciplinas import disciplinas
from .site import site
from .aluno import aluno
from .docente import docente
import click


@click.group('cli')
def cli():
    ...


cli.add_command(disciplinas)
cli.add_command(site)
cli.add_command(aluno)
cli.add_command(docente)

cli()
