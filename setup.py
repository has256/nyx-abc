from setuptools import setup

setup(
    name='nyx',
    version='0.0.1',
    packages=[
        'nyx',
        'nyx.student',
        'nyx.student.adapters',
        'nyx.student.adapters.http',
        'nyx.student.models',
        'nyx.student.services',
        'nyx.professor',
        'nyx.professor.adapters',
        'nyx.professor.adapters.http',
        'nyx.professor.models',
        'nyx.professor.services',
        'nyx.website',
        'nyx.website.models',
    ],
    entry_points={
        'console_scripts':
            ['nyx = nyx:cli']
    }
)
