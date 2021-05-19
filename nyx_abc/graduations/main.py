from nyx_abc.graduations.config.cmcc import BCC, BNC, BM, LMAT
from nyx_abc.graduations.config.interdisciplinary import BCT
import click
import json


@click.group('cursos')
def cursos():
    """Utilitarios de Graduações"""
    ...


@cursos.command()
@click.argument('curso')
def grade_ideal(curso):
    """Retorna a grade curricular em quadrimestres sugeridos para os cursos da UFABC"""
    graduation = curso

    if graduation.lower() in ['bcc', 'comp', 'computacao']:
        print_quarter(BCC.subjects)
    elif graduation.lower() in ['bnc', 'neuro', 'neurociencia']:
        print_quarter(BNC.subjects)
    elif graduation.lower() in ['bm', 'matematica', 'matemagica']:
        print_quarter(BM.subjects)
    elif graduation.lower() in ['licenciatura em matematica', ' licenciatura matematica', 'lmat']:
        print_quarter(LMAT.subjects)
    elif graduation.lower() in ['bct', 'ciencia e tecnologia', 'bc&t', 'inferno']:
        print_quarter(BCT.subjects)


def print_quarter(graduation):
    for quarter, subjects in graduation.items():
        click.secho(quarter, fg='red')
        for i, subject in enumerate(subjects):
            click.echo(subject)
            if i + 1 == len(subjects):
                click.echo('')
