# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Processadora paySmart - API de integração com emissores",
    author_email="atendimento@paysmart.com.br",
    url="",
    keywords=["Swagger", "Processadora paySmart - API de integração com emissores"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    API de integração com emissores paySmart contém funções que compreendem desde a solicitação de inclusão de novas contas e cartões, pedidos de crédito, funções de atendimento e intercâmbio, associação de CPF à conta e cartão, bloqueio e desbloqueio de cartões até o envio de extrato mensal.
    """
)
