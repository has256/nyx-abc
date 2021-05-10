from setuptools import setup

setup(
    name='nyx',
    version='0.0.1',
    packages=[
        'nyx',
        'nyx.student',
        'nyx.student.adapter',
        'nyx.student.adapter.http',
        'nyx.student.models',
        'nyx.student.service',
        'nyx.professor',
        'nyx.professor.adapter',
        'nyx.professor.adapter.http',
        'nyx.professor.models',
        'nyx.professor.service',
        'nyx.website',
        'nyx.website.models',
    ],
    entry_points={
        'console_scripts':
            ['nyx = nyx:cli']
    }
)
