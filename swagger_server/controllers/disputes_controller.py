import connexion
import six

from swagger_server.models.dispute import Dispute  # noqa: E501
from swagger_server.models.dispute_code import DisputeCode  # noqa: E501
from swagger_server.models.dispute_created_successfully import DisputeCreatedSuccessfully  # noqa: E501
from swagger_server.models.dispute_list_result import DisputeListResult  # noqa: E501
from swagger_server.models.dispute_request import DisputeRequest  # noqa: E501
from swagger_server.models.dispute_response_created_successfully import DisputeResponseCreatedSuccessfully  # noqa: E501
from swagger_server.models.dispute_response_request import DisputeResponseRequest  # noqa: E501
from swagger_server.models.dispute_reversal_created_successfully import DisputeReversalCreatedSuccessfully  # noqa: E501
from swagger_server.models.dispute_reversal_request import DisputeReversalRequest  # noqa: E501
from swagger_server.models.dispute_status import DisputeStatus  # noqa: E501
from swagger_server.models.result_data import ResultData  # noqa: E501
from swagger_server import util


def add_dispute(body, idempotency_key=None):  # noqa: E501
    """Registra uma disputa para questionar a validade de uma transação.

     # noqa: E501

    :param body: Dados do registro de disputa.
    :type body: dict | bytes
    :param idempotency_key: A API suporta idempotência para que, após um erro de conexão, por exemplo, se possa tentar novamente requisições POST sem acidentalmente efetuar a mesma operação duas vezes. Para indicar uma requisição é idempotente, envie uma IdempotencyKey no header da requisição com uma chave única (recomendamos UUIDs V4).
    :type idempotency_key: 

    :rtype: DisputeCreatedSuccessfully
    """
    if connexion.request.is_json:
        body = DisputeRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_disputes(beginning_date, ending_date, limit=None, starting_after=None, ending_before=None, dispute_reason=None, dispute_status=None):  # noqa: E501
    """Recupera uma lista de disputas do emissor de acordo com os filtros definidos.

     # noqa: E501

    :param beginning_date: Data indicando o primeiro dia cujos dados devem ser retornados.
    :type beginning_date: str
    :param ending_date: Data indicando o último dia cujos dados devem ser retornados.
    :type ending_date: str
    :param limit: Número limite de objetos retornados. O valor deve ser entre 1 e 100.
    :type limit: int
    :param starting_after: Um cursor para uso em paginação. {starting_after} é o identificador único do objeto a partir do qual se quer listar. Por exemplo, se houve um retorno de uma lista de 100 objetos para esta chamada sendo que o último possui identificador \&quot;obj1234\&quot;, para se obter a página use \&quot;starting_after&#x3D;obj1234\&quot;.
    :type starting_after: str
    :param ending_before: Um cursor para uso em paginação. {ending_before} é o identificador único do objeto a partir do qual se quer listar os anteriores. Por exemplo, se houve um retorno de uma lista de 100 objetos para esta chamada sendo que o primeiro possui identificador \&quot;obj1234\&quot;, para se obter a página anterior use \&quot;ending_before&#x3D;obj1234\&quot;.
    :type ending_before: str
    :param dispute_reason: Código do motivo das disputas a serem retornadas.
    :type dispute_reason: dict | bytes
    :param dispute_status: Status das disputas a serem retornadas.
    :type dispute_status: dict | bytes

    :rtype: DisputeListResult
    """
    if connexion.request.is_json:
        dispute_reason = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        dispute_status = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_dispute(dispute_id):  # noqa: E501
    """Recupera informações de uma disputa.

     # noqa: E501

    :param dispute_id: Identificador da disputa.
    :type dispute_id: str

    :rtype: Dispute
    """
    return 'do some magic!'


def repond_dispute(body, dispute_id, idempotency_key=None):  # noqa: E501
    """Responde a um parecer negativo da bandeira/credenciador. A resposta pode aceitar o parcer e desistir da disputa ou pode discordar e passar a disputa para a próxima fase.

     # noqa: E501

    :param body: Uma resposta a uma negativa por parte do credenciador, indicado aceitação ou continuação do processo de disputa e incluidno motivos no caso de continuação.
    :type body: dict | bytes
    :param dispute_id: Identificador da disputa.
    :type dispute_id: str
    :param idempotency_key: A API suporta idempotência para que, após um erro de conexão, por exemplo, se possa tentar novamente requisições POST sem acidentalmente efetuar a mesma operação duas vezes. Para indicar uma requisição é idempotente, envie uma IdempotencyKey no header da requisição com uma chave única (recomendamos UUIDs V4).
    :type idempotency_key: 

    :rtype: DisputeResponseCreatedSuccessfully
    """
    if connexion.request.is_json:
        body = DisputeResponseRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def undo_dispute(body, dispute_id, idempotency_key=None):  # noqa: E501
    """Desiste de uma disputa e envia uma reversão dela.

     # noqa: E501

    :param body: Dados para reversão do pedido de disputa.
    :type body: dict | bytes
    :param dispute_id: Identificador da disputa.
    :type dispute_id: str
    :param idempotency_key: A API suporta idempotência para que, após um erro de conexão, por exemplo, se possa tentar novamente requisições POST sem acidentalmente efetuar a mesma operação duas vezes. Para indicar uma requisição é idempotente, envie uma IdempotencyKey no header da requisição com uma chave única (recomendamos UUIDs V4).
    :type idempotency_key: 

    :rtype: DisputeReversalCreatedSuccessfully
    """
    if connexion.request.is_json:
        body = DisputeReversalRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
