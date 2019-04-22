# -*- coding: utf-8 -*-

# Learn more: https://github.com/adrixo/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Teoría de códigos',
    version='0.2',
    description='Interfaz básica para instanciación y manejo de códigos',
    long_description=readme,
    author='Adrián Valera',
    author_email='adrianvalrom@gmail.com',
    url='https://github.com/adrixo/codigos',
    license=license,
    packages=find_packages()
)
