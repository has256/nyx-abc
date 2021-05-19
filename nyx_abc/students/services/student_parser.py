import click
from nyx.students.models.student_model import Student


class StudentParser():

    @classmethod
    def parse(cls, response):
        student = Student(response["fullname"],
                          response["username"], response["email"][0])
        click.echo(student)
