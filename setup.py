from setuptools import setup
setup(
    name = 'dojo',
    version = '1.0.0',
    packages = ['dojo'],
    entry_points = {
        'console_scripts': [
            'dojo = dojo.__main__:main'
        ]
    })