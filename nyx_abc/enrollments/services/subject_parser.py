import click
from nyx_abc.enrollments.models.subject_model import Subject


class SubjectParser():

    @classmethod
    def parse_name(cls, response):
        subject = get_subject(response)
        return subject.name

    @classmethod
    def parse_slots_freshmen(cls, response):
        subject = get_subject(response)
        return subject.slots_freshmen

    @classmethod
    def parse_id(cls, response):
        subject = get_subject(response)
        return str(subject.subject_id)

    @classmethod
    def parse_slots(cls, response):
        subject = get_subject(response)
        return subject.slots


def get_subject(response, enrollments=None):
    return Subject(response["id"],
                   response["nome"],
                   response["vagas"],
                   response["vagas_ingressantes"])
