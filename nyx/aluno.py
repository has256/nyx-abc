from pathlib import Path
import click
import requests
import json
import re
import pandas as pd


@click.group('aluno')
def aluno():
    """Utilitarios de Alunos(as)"""
    ...


@aluno.command()
@click.argument('ra')
def nome_completo(ra):
    """Retorna o nome completo de alunos(as) usando seu RA"""
    res = requests.get(
        f'https://sig.ufabc.edu.br/sigaa/APISistemasNTI?funcao=2&valor={ra}')
    nome = json.loads(res.text)
    click.echo(nome['fullname'])


@aluno.command()
@click.argument('ra')
def email(ra):
    """Retorna o e-mail de alunos(as) usando seu RA"""
    res = requests.get(
        f'https://sig.ufabc.edu.br/sigaa/APISistemasNTI?funcao=2&valor={ra}')
    nome = json.loads(res.text)
    click.echo(nome['email'][0])

@aluno.command()
@click.argument('arg')
def info(arg):
    """Retorna infos completas usando RA, usuario ou email como argumento"""
    res = requests.get(
        f'https://sig.ufabc.edu.br/sigaa/APISistemasNTI?funcao=2&valor={arg}')
    nome = json.loads(res.text)
    click.echo(f"Nome: {nome['fullname']}, username: {nome['username']}, email: {nome['email'][0]}")
