from enum import Enum
import click


Url = str
SubCommand = click.core.Command
CommandGroup = click.core.Command


class WebsitesUFABC(Enum):

    bcc: Url = 'https://bcc.ufabc.edu.br'
    gradmat: Url = 'https://gradmat.ufabc.edu.br/'
    moodle: Url = 'https://moodle.ufabc.edu.br/'
    neuro: Url = 'https://neuro.ufabc.edu.br/'
    prograd: Url = 'https://prograd.ufabc.edu.br/'
    sigaa: Url = 'https://sig.ufabc.edu.br/sigaa/verTelaLogin.do'
    tidia: Url = 'https://tidia4.ufabc.edu.br/portal/relogin'
    ufabc: Url = 'https://www.ufabc.edu.br/'


def make_website_subcommand(name: str, url: Url) -> SubCommand:

    fn_template: str = f'''@site.command()
def {name}():
    """Abre o site do(a) {name}"""
    click.launch('{url}')
    '''

    exec(fn_template)
    website_subcommand: SubCommand = locals()[f'{name}']

    return website_subcommand


@ click.group('site')
def site() -> CommandGroup:
    """Utilitarios de Sites da UFABC"""
    ...


for website in WebsitesUFABC:
    make_website_subcommand(website.name, website.value)
