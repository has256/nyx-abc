from enum import Enum

Url = str


class WebsitesModel(Enum):

    bcc: Url = 'https://bcc.ufabc.edu.br'
    gradmat: Url = 'https://gradmat.ufabc.edu.br/'
    moodle: Url = 'https://moodle.ufabc.edu.br/'
    neuro: Url = 'https://neuro.ufabc.edu.br/'
    prograd: Url = 'https://prograd.ufabc.edu.br/'
    sigaa: Url = 'https://sig.ufabc.edu.br/sigaa/verTelaLogin.do'
    tidia: Url = 'https://tidia4.ufabc.edu.br/portal/relogin'
    ufabc: Url = 'https://www.ufabc.edu.br/'
