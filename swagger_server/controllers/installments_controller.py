import connexion
import six

from swagger_server.models.advance_payment_request import AdvancePaymentRequest  # noqa: E501
from swagger_server.models.all_installment_purchase import AllInstallmentPurchase  # noqa: E501
from swagger_server.models.installment_options import InstallmentOptions  # noqa: E501
from swagger_server.models.installment_request import InstallmentRequest  # noqa: E501
from swagger_server.models.result_data import ResultData  # noqa: E501
from swagger_server import util


def advance_payment(body, account_id, idempotency_key=None):  # noqa: E501
    """Pedido de liquidação antecipada de parcelas futuras.

    Cria um pedido de liquidação antecipada de um número de parcelas futuras de uma determinada compra. # noqa: E501

    :param body: Dados para a liquidação antecipada, incluindo a compra e quantidade de faturas.
    :type body: dict | bytes
    :param account_id: Identificador da conta.
    :type account_id: str
    :param idempotency_key: A API suporta idempotência para que, após um erro de conexão, por exemplo, se possa tentar novamente requisições POST sem acidentalmente efetuar a mesma operação duas vezes. Para indicar uma requisição é idempotente, envie uma IdempotencyKey no header da requisição com uma chave única (recomendamos UUIDs V4).
    :type idempotency_key: 

    :rtype: ResultData
    """
    if connexion.request.is_json:
        body = AdvancePaymentRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_account_statement_closed_installment_options(account_id):  # noqa: E501
    """Recupera informações sobre possibilidade de parcelamento de saldo devedor que já completou 30 dias de rotativo.

    Retorna todos os dados sobre as possibilidades de parcelamento de qualquer saldo devedor que já esteja completando 30 dias no crédito rotativo. # noqa: E501

    :param account_id: Identificador da conta.
    :type account_id: str

    :rtype: InstallmentOptions
    """
    return 'do some magic!'


def get_future_installments(account_id):  # noqa: E501
    """Recupera informações sobre compras parceladas que ainda tem parcelas no futuro.

    Retorna todos os dados de compras parceladas que ainda tenham parcelas que irão vencer no futuro. # noqa: E501

    :param account_id: Identificador da conta.
    :type account_id: str

    :rtype: AllInstallmentPurchase
    """
    return 'do some magic!'


def installment_request(body, account_id, idempotency_key=None):  # noqa: E501
    """Pedido de parcelamento de saldo devedor.

    Cria um pedido de parcelamento do saldo devedor, de acordo com uma das opções préviamente definidas. # noqa: E501

    :param body: Dados da opção de parcelamento sendo requisitada.
    :type body: dict | bytes
    :param account_id: Identificador da conta.
    :type account_id: str
    :param idempotency_key: A API suporta idempotência para que, após um erro de conexão, por exemplo, se possa tentar novamente requisições POST sem acidentalmente efetuar a mesma operação duas vezes. Para indicar uma requisição é idempotente, envie uma IdempotencyKey no header da requisição com uma chave única (recomendamos UUIDs V4).
    :type idempotency_key: 

    :rtype: ResultData
    """
    if connexion.request.is_json:
        body = InstallmentRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
