from setuptools import setup

setup(
    name='nyx',
    version='0.0.1',
    packages=[
        'nyx',
        'nyx.enrollments',
        'nyx.enrollments.adapters',
        'nyx.enrollments.adapters.http',
        'nyx.enrollments.models',
        'nyx.enrollments.services',
        'nyx.graduations',
        'nyx.graduations.config',
        'nyx.graduations.config.cmcc',
        'nyx.graduations.config.ccnh',
        'nyx.graduations.config.cecs',
        'nyx.graduations.config.interdisciplinary',
        'nyx.students',
        'nyx.students.adapters',
        'nyx.students.adapters.http',
        'nyx.students.models',
        'nyx.students.services',
        'nyx.professors',
        'nyx.professors.adapters',
        'nyx.professors.adapters.http',
        'nyx.professors.models',
        'nyx.professors.services',
        'nyx.websites',
        'nyx.websites.models',
        'nyx.enrollments',
        'nyx.subjects'
    ],
    entry_points={
        'console_scripts':
            ['nyx = nyx:cli']
    }
)
