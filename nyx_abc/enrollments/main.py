from nyx_abc.enrollments.adapters.http.current_subjects_client import SubjectsClient
from nyx_abc.enrollments.adapters.http.enrollments_client import EnrollmentsClient
from nyx_abc.enrollments.adapters.http.summary_client import SummaryClient
from nyx_abc.enrollments.services.subject_parser import SubjectParser
import click
import time


@click.group('matriculas')
def matriculas():
    """Utilitarios de Matriculas"""
    ...


@matriculas.command()
@click.option('--username', prompt=True)
@click.option('--password', prompt=True, hide_input=True)
def minha_grade(username, password):
    """Retorna a grade atual do resumo passando login/senha"""
    subjects_with_schedule = SummaryClient.get_my_subjects(username, password)
    for i, subject in enumerate(subjects_with_schedule):
        click.echo(f'\n{subject[0]}')
        for j, time in enumerate(subject[1]):
            click.echo(f'{time}')


@matriculas.command()
@click.option('--ingressantes', is_flag=True)
def ofertadas(ingressantes):
    """Retorna as disciplinas ofertadas do sistema"""

    subjects = SubjectsClient.get_all_current_subjects()

    freshman = ingressantes

    for subject in subjects['body']:

        if not freshman:
            subject_name = SubjectParser.parse_name(subject)
            click.echo(subject_name)
        if SubjectParser.parse_slots_freshmen(subject) is not None:
            subject_name = SubjectParser.parse_name(subject)
            click.echo(subject_name)


@matriculas.command()
def alta_demanda():
    """Retorna as disciplinas de alta demanda do sistema"""

    subjects = SubjectsClient.get_all_current_subjects()
    enrollments = EnrollmentsClient.get_enrollments_counter()

    enrollments_counter = enrollments['body']
    enrollments_ids = enrollments_counter.keys()

    for subject in subjects['body']:

        subject_id = SubjectParser.parse_id(subject)
        subject_slots = SubjectParser.parse_slots(subject)
        subject_name = SubjectParser.parse_name(subject)

        if subject_id in enrollments_ids:

            enrollments_count = enrollments_counter[subject_id]

            if enrollments_count >= (15 * subject_slots / 10):
                click.echo(subject_name)


@matriculas.command()
def vazias():
    """Retorna as disciplinas vazias do sistema"""

    subjects = SubjectsClient.get_all_current_subjects()
    enrollments = EnrollmentsClient.get_enrollments_counter()

    enrollments_counter = enrollments['body']
    enrollments_ids = enrollments_counter.keys()

    for subject in subjects['body']:

        subject_id = SubjectParser.parse_id(subject)
        subject_slots = SubjectParser.parse_slots(subject)
        subject_name = SubjectParser.parse_name(subject)

        if subject_id in enrollments_ids:
            enrollments_count = enrollments_counter[subject_id]
            if int(enrollments_count) < subject_slots:
                click.echo(subject_name)


@matriculas.command()
def watch():
    '''Acompanha o sistema de matriculas real-time'''
    while True:
        old_response = get_subject_with_enrollments()
        time.sleep(2)
        new_response = get_subject_with_enrollments()
        if old_response == new_response:
            print('Nothing Changed')
        else:
            print('Changed!!!')
            for i, subject in enumerate(new_response):
                if subject[1] != old_response[i][1]:
                    print(f'{subject[0]} tem {subject[1]} vagas')


def get_subject_with_enrollments():

    subjects = SubjectsClient.get_all_current_subjects()
    enrollments = EnrollmentsClient.get_enrollments_counter()

    enrollments_counter = enrollments['body']
    enrollments_ids = enrollments_counter.keys()

    resultado = []

    for subject in subjects['body']:

        subject_id = SubjectParser.parse_id(subject)
        subject_slots = SubjectParser.parse_slots(subject)
        subject_name = SubjectParser.parse_name(subject)
        enrollments_count = enrollments_counter[subject_id]

        if subject_id in enrollments_ids:
            resultado.append(
                (subject_name, subject_slots - int(enrollments_count)))

    return resultado
