from pathlib import Path
import click
import requests
import json
import re
import pandas as pd


@click.group('docente')
def docente():
    """Utilitarios de Docentes"""
    ...


@docente.command()
@click.argument('email')
def nome_completo(email):
    """Retorna o nome completo de docentes usando seu e-mail"""
    user = email.split("@")[0]
    res = requests.get(
        f'https://sig.ufabc.edu.br/sigaa/APISistemasNTI?funcao=1&valor={user}')
    nome = json.loads(res.text)
    click.echo(nome['nome'])


@docente.command()
@click.argument('email')
def siape(email):
    """Retorna o SIAPE de docentes usando seu e-mail"""
    user = email.split("@")[0]
    res = requests.get(
        f'https://sig.ufabc.edu.br/sigaa/APISistemasNTI?funcao=1&valor={user}')
    nome = json.loads(res.text)
    click.echo(nome['siape'])
