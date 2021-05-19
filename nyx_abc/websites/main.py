from nyx_abc.websites.models.site_model import WebsitesModel
import click

Url = str
SubCommand = click.core.Command
CommandGroup = click.core.Command


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


for website in WebsitesModel:
    make_website_subcommand(website.name, website.value)
