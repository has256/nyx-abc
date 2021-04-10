import click
import requests
import re
import pandas as pd


@click.group('disciplinas')
def disciplinas():
    """Utilitarios de Disciplinas"""
    ...


@disciplinas.command()
@click.option('--ingressantes', is_flag=True)
def ofertadas(ingressantes):
    """Retorna as disciplinas ofertadas do sistema"""
    todas_disciplinas = requests.get(
        'https://matricula.ufabc.edu.br/cache/todasDisciplinas.js')
    disciplinas_ofertadas = todas_disciplinas.content.decode("utf-8")[17:-2]
    disciplinas_ofertadas = re.sub('null', 'None', disciplinas_ofertadas)
    disciplinas_ofertadas = eval(disciplinas_ofertadas)
    for disciplina in disciplinas_ofertadas:
        if not ingressantes:
            click.echo(disciplina['nome'])
            continue
        if disciplina['vagas_ingressantes'] is not None:
            click.echo(disciplina['nome'])
