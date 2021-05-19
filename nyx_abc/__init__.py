from nyx_abc.students.main import aluno
from nyx_abc.professors.main import docente
from nyx_abc.websites.main import site
from nyx_abc.enrollments.main import matriculas
from nyx_abc.subjects.main import ementas
from nyx_abc.graduations.main import cursos
import click


@click.group('cli')
def cli():
    ...


cli.add_command(matriculas)
cli.add_command(site)
cli.add_command(aluno)
cli.add_command(docente)
cli.add_command(ementas)
cli.add_command(cursos)

cli()
