import click


@click.group('site')
def site():
    """Utilitarios de Sites da UFABC"""
    ...


@site.command()
def prograd():
    """Abre o site da trollgrad"""
    click.launch('https://prograd.ufabc.edu.br/')


@site.command()
def sigaa():
    """Abre o SIGAA - o site mais bugado do brasil"""
    click.launch('https://sig.ufabc.edu.br/sigaa/verTelaLogin.do')


@site.command()
def moodle():
    """Abre o moodle"""
    click.launch('https://moodle.ufabc.edu.br/')


@site.command()
def gradmat():
    """Abre o gradmat"""
    click.launch('https://gradmat.ufabc.edu.br/')


@site.command()
def ufabc():
    """Abre o site da ufabc"""
    click.launch('https://www.ufabc.edu.br/')


@site.command()
def bcc():
    """Abre o site do bcc"""
    click.launch('https://bcc.ufabc.edu.br')


@site.command()
def neuro():
    """Abre o site da neuro"""
    click.launch('https://neuro.ufabc.edu.br/')
