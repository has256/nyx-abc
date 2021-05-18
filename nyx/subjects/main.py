import click
import pandas as pd
import os


@click.command('ementas')
@click.argument('disciplina')
@click.option('--bibliografia', is_flag=True)
def ementas(disciplina, bibliografia):
    """Utilitarios de Ementas"""
    ementas = pd.read_excel(
        "https://github.com/EduRenesto/ufabc-manpages/blob/master/disciplinas.xlsx?raw=true")
    query = ementas.query(
        f'DISCIPLINA.str.contains("{disciplina}")', engine='python')
    for index, row in query.iterrows():
        click.secho(row.DISCIPLINA + ":", fg='blue')
        click.secho(
            f"TPI: {row.TPI}, Recomendação: {row.RECOMENDAÇÃO}", fg='red')
        if bibliografia:
            click.secho("Bibliografia Sugerida:", fg='green', underline=True)
            click.secho(f"{row['BIBLIOGRAFIA BÁSICA']}\n", fg='green')
        click.secho("Ementa:", fg='green', underline=True)
        click.secho(f"{row.EMENTA}\n", fg='green')
        click.secho(f"-"*78, fg='yellow')


@click.command('ementas')
@click.argument('disciplina')
@click.option('--bibliografia', is_flag=True)
def baixar_ementa(disciplina, bibliografia):
    """Utilitarios de Ementas"""
    ementas = pd.read_excel(
        "https://github.com/EduRenesto/ufabc-manpages/blob/master/disciplinas.xlsx?raw=true")
    query = ementas.query(
        f'DISCIPLINA.str.contains("{disciplina}")', engine='python')
    for index, row in query.iterrows():
        click.secho(row.DISCIPLINA + ":", fg='blue')
        click.secho(
            f"TPI: {row.TPI}, Recomendação: {row.RECOMENDAÇÃO}", fg='red')
        if bibliografia:
            click.secho("Bibliografia Sugerida:", fg='green', underline=True)
            click.secho(f"{row['BIBLIOGRAFIA BÁSICA']}\n", fg='green')
        click.secho("Ementa:", fg='green', underline=True)
        click.secho(f"{row.EMENTA}\n", fg='green')
        click.secho(f"-"*78, fg='yellow')
