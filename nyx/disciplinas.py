import click
import requests
import pandas as pd
import json


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
    disciplinas_ofertadas = json.loads(disciplinas_ofertadas)
    for disciplina in disciplinas_ofertadas:
        if not ingressantes:
            click.echo(disciplina['nome'])
            continue
        if disciplina['vagas_ingressantes'] is not None:
            click.echo(disciplina['nome'])


@disciplinas.command()
def alta_demanda():
    """Retorna as disciplinas de alta demanda do sistema"""

    todas_disciplinas = requests.get(
        'https://matricula.ufabc.edu.br/cache/todasDisciplinas.js')
    disciplinas_ofertadas = todas_disciplinas.content.decode("utf-8")[17:-2]
    disciplinas_ofertadas = json.loads(disciplinas_ofertadas)

    contagem_disciplinas = requests.get(
        'https://matricula.ufabc.edu.br/cache/contagemMatriculas.js')
    contagem_disciplinas = contagem_disciplinas.content.decode("utf-8")[19:-2]
    contagem_disciplinas = json.loads(contagem_disciplinas)

    for disciplina in disciplinas_ofertadas:
        if str(disciplina['id']) in contagem_disciplinas.keys():
            requisicoes = contagem_disciplinas[str(disciplina['id'])]
            if int(requisicoes) >= (15*disciplina['vagas']/10):
                print(disciplina['nome'])


@disciplinas.command()
def vazia():
    """Retorna as disciplinas vazias do sistema"""

    todas_disciplinas = requests.get(
        'https://matricula.ufabc.edu.br/cache/todasDisciplinas.js')
    disciplinas_ofertadas = todas_disciplinas.content.decode("utf-8")[17:-2]
    disciplinas_ofertadas = json.loads(disciplinas_ofertadas)

    contagem_disciplinas = requests.get(
        'https://matricula.ufabc.edu.br/cache/contagemMatriculas.js')
    contagem_disciplinas = contagem_disciplinas.content.decode("utf-8")[19:-2]
    contagem_disciplinas = json.loads(contagem_disciplinas)

    for disciplina in disciplinas_ofertadas:
        if str(disciplina['id']) in contagem_disciplinas.keys():
            requisicoes = contagem_disciplinas[str(disciplina['id'])]
            if int(requisicoes) < (disciplina['vagas']):
                print(disciplina['nome'])
