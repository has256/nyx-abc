from nyx.students.main import aluno
from nyx.professors.main import docente
from nyx.websites.main import site
from nyx.enrollments.main import matriculas
from nyx.subjects.main import ementas
import click


@click.group('cli')
def cli():
    ...


cli.add_command(matriculas)
cli.add_command(site)
cli.add_command(aluno)
cli.add_command(docente)
cli.add_command(ementas)

cli()
