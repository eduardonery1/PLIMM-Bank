import connexion
import six

from swagger_server.models.cancel_virtual_card_request import CancelVirtualCardRequest  # noqa: E501
from swagger_server.models.cancel_virtual_card_response import CancelVirtualCardResponse  # noqa: E501
from swagger_server.models.create_virtual_card_request import CreateVirtualCardRequest  # noqa: E501
from swagger_server.models.create_virtual_card_response import CreateVirtualCardResponse  # noqa: E501
from swagger_server.models.get_virtual_card_response import GetVirtualCardResponse  # noqa: E501
from swagger_server.models.list_virtual_cards_response import ListVirtualCardsResponse  # noqa: E501
from swagger_server.models.result_data import ResultData  # noqa: E501
from swagger_server import util


def cancel_virtual_card(body, v_card_id, idempotency_key=None):  # noqa: E501
    """Cancela um cartão virtual.

     # noqa: E501

    :param body: Informações de cancelamento do CV.
    :type body: dict | bytes
    :param v_card_id: Identificador do cartão virtual.
    :type v_card_id: str
    :param idempotency_key: A API suporta idempotência para que, após um erro de conexão, por exemplo, se possa tentar novamente requisições POST sem acidentalmente efetuar a mesma operação duas vezes. Para indicar uma requisição é idempotente, envie uma IdempotencyKey no header da requisição com uma chave única (recomendamos UUIDs V4).
    :type idempotency_key: 

    :rtype: CancelVirtualCardResponse
    """
    if connexion.request.is_json:
        body = CancelVirtualCardRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_virtual_card(body, card_id, idempotency_key=None):  # noqa: E501
    """Cria um novo cartão virtual.

     # noqa: E501

    :param body: Especificações do cartão virtual solicitado.
    :type body: dict | bytes
    :param card_id: Identificador do cartão.
    :type card_id: str
    :param idempotency_key: A API suporta idempotência para que, após um erro de conexão, por exemplo, se possa tentar novamente requisições POST sem acidentalmente efetuar a mesma operação duas vezes. Para indicar uma requisição é idempotente, envie uma IdempotencyKey no header da requisição com uma chave única (recomendamos UUIDs V4).
    :type idempotency_key: 

    :rtype: CreateVirtualCardResponse
    """
    if connexion.request.is_json:
        body = CreateVirtualCardRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_virtual_card(v_card_id):  # noqa: E501
    """Lista todos os cartões virtuais para um determinado cartão real

     # noqa: E501

    :param v_card_id: Identificador do cartão virtual.
    :type v_card_id: str

    :rtype: GetVirtualCardResponse
    """
    return 'do some magic!'


def list_virtual_cards(card_id):  # noqa: E501
    """Lista todos os cartões virtuais para um determinado cartão real

     # noqa: E501

    :param card_id: Identificador do cartão.
    :type card_id: str

    :rtype: ListVirtualCardsResponse
    """
    return 'do some magic!'
