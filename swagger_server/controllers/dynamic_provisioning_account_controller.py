import connexion
import six

from swagger_server.models.balance import Balance  # noqa: E501
from swagger_server.models.credit_list_mattress import CreditListMattress  # noqa: E501
from swagger_server.models.result_data import ResultData  # noqa: E501
from swagger_server import util


def get_balance():  # noqa: E501
    """Solicita informação de saldo na conta colchão.

     # noqa: E501


    :rtype: Balance
    """
    return 'do some magic!'


def get_credits(beginning_date, end_date):  # noqa: E501
    """Obtém uma lista de aportes realizados nos dias especificados.

     # noqa: E501

    :param beginning_date: Data indicando o primeiro dia cujos dados devem ser retornados.
    :type beginning_date: str
    :param end_date: Data indicando o último dia cujos dados devem ser retornados.
    :type end_date: str

    :rtype: CreditListMattress
    """
    return 'do some magic!'
