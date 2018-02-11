from setuptools import setup

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='py-template',
    version='0.0.1',
    description='A template for python development',
    long_description=long_description,
    url='https://github.com/wasbazi/py-template',
    author='Avi',

    author_email='wasbazi@gmail.com',

    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=[
        'flask',
        'sqlalchemy',
        'flask-sqlalchemy',
        # 'mysqlclient',
    ],
    # extras_require={  # Optional
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },
)
