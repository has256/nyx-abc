import click
import requests
import pandas as pd
import json
import time


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


@disciplinas.command()
def watch():
    '''Acompanha o sistema de matriculas real-time'''
    while True:
        old_disciplinas = get_disciplina()
        time.sleep(5)
        new_disciplinas = get_disciplina()
        if old_disciplinas == new_disciplinas:
            print('Nothing Changed')
        else:
            print('Changed!!!')
            for i, disciplina in enumerate(new_disciplinas):
                if disciplina[1] != old_disciplinas[i][1]:
                    print(f'{disciplina[0]} tem {disciplina[1]} vagas')


def get_disciplina():
    todas_disciplinas = requests.get(
        'https://matricula.ufabc.edu.br/cache/todasDisciplinas.js')
    disciplinas_ofertadas = todas_disciplinas.content.decode("utf-8")[17:-2]
    disciplinas_ofertadas = json.loads(disciplinas_ofertadas)

    contagem_disciplinas = requests.get(
        'https://matricula.ufabc.edu.br/cache/contagemMatriculas.js')
    contagem_disciplinas = contagem_disciplinas.content.decode("utf-8")[19:-2]
    contagem_disciplinas = json.loads(contagem_disciplinas)

    resultado = []

    for disciplina in disciplinas_ofertadas:
        if str(disciplina['id']) in contagem_disciplinas.keys():
            resultado.append(
                (disciplina['nome'], disciplina['vagas'] - int(contagem_disciplinas[str(disciplina['id'])])))

    return resultado
