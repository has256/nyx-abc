from enum import Enum
import click


class WebsitesUFABC(Enum):
    bcc = 'https://bcc.ufabc.edu.br'
    gradmat = 'https://gradmat.ufabc.edu.br/'
    moodle = 'https://moodle.ufabc.edu.br/'
    neuro = 'https://neuro.ufabc.edu.br/'
    prograd = 'https://prograd.ufabc.edu.br/'
    sigaa = 'https://sig.ufabc.edu.br/sigaa/verTelaLogin.do'
    tidia = 'https://tidia4.ufabc.edu.br/portal/relogin'
    ufabc = 'https://www.ufabc.edu.br/'


def make_website_subcommand(name, url):

    exec(
        f'''@site.command()\ndef {name}():\n\t"""Abre o site do(a) {name}"""\n\tclick.launch('{url}')'''
    )

    return locals()[f'{name}']


@ click.group('site')
def site():
    """Utilitarios de Sites da UFABC"""
    ...


for website in WebsitesUFABC:
    make_website_subcommand(website.name, website.value)
