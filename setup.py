from setuptools import setup

setup(
    name='nyx',
    version='0.0.1',
    packages=['nyx'],
    entry_points={
        'console_scripts':
            ['nyx = nyx:cli']
    }
)
