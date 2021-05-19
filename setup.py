from setuptools import setup

setup(
    name='nyx-abc',
    version='0.1.0',
    license='MIT',
    author='Carlos EA. Batista',
    author_email='cardu.chmod.777@gmail.com',
    url='https://github.com/has256/nyx-abc',
    download_url='https://github.com/has256/nyx-abc/0.1.0.tar.gz',
    keywords=['nyx', 'CLI APP', 'UFABC'],
    packages=[
        'nyx_abc',
        'nyx_abc.enrollments',
        'nyx_abc.enrollments.adapters',
        'nyx_abc.enrollments.adapters.http',
        'nyx_abc.enrollments.models',
        'nyx_abc.enrollments.services',
        'nyx_abc.graduations',
        'nyx_abc.graduations.config',
        'nyx_abc.graduations.config.cmcc',
        'nyx_abc.graduations.config.ccnh',
        'nyx_abc.graduations.config.cecs',
        'nyx_abc.graduations.config.interdisciplinary',
        'nyx_abc.students',
        'nyx_abc.students.adapters',
        'nyx_abc.students.adapters.http',
        'nyx_abc.students.models',
        'nyx_abc.students.services',
        'nyx_abc.professors',
        'nyx_abc.professors.adapters',
        'nyx_abc.professors.adapters.http',
        'nyx_abc.professors.models',
        'nyx_abc.professors.services',
        'nyx_abc.websites',
        'nyx_abc.websites.models',
        'nyx_abc.enrollments',
        'nyx_abc.subjects'
    ],
    entry_points={
        'console_scripts':
            ['nyx-abc = nyx:cli']
    },
    install_requires=[
        'click==7.1.2',
        'requests==2.25.1',
        'lxml==4.6.2',
        'pandas==1.2.3',
        'xlrd==1.2.0',
        'unidecode==1.2.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
