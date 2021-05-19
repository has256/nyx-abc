from setuptools import setup

setup(
    name='nyx',
    version='0.1.0',
    license='MIT',
    author='Carlos EA. Batista',
    author_email='cardu.chmod.777@gmail.com',
    url='https://github.com/has256/nyx',
    download_url='https://github.com/has256/nyx/v_01.tar.gz',
    keywords=['CLI APP', 'UFABC'],
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
