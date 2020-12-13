import connexion
import six

from swagger_server.models.credit_created_successfully import CreditCreatedSuccessfully  # noqa: E501
from swagger_server.models.credit_list_result import CreditListResult  # noqa: E501
from swagger_server.models.entry_mode import EntryMode  # noqa: E501
from swagger_server.models.new_credit_request import NewCreditRequest  # noqa: E501
from swagger_server.models.result_data import ResultData  # noqa: E501
from swagger_server.models.transaction import Transaction  # noqa: E501
from swagger_server.models.transaction_list_result import TransactionListResult  # noqa: E501
from swagger_server.models.transaction_status import TransactionStatus  # noqa: E501
from swagger_server.models.transaction_type import TransactionType  # noqa: E501
from swagger_server import util


def add_credit(body, account_id, idempotency_key=None):  # noqa: E501
    """Registra uma nova carga de créditos com data de efetivação.

    Solicita registro de uma nova carga de créditos para a conta com identificador {accountId}. A carga de crédito tem uma data de efetivação. A data pode ser no dia atual, no futuro (crédito agendado) ou no passado (indicando um pagamento recebido anteriormente). # noqa: E501

    :param body: Informações relacionadas à carga de créditos para inclusão na processadora paySmart.
    :type body: dict | bytes
    :param account_id: Identificador da conta.
    :type account_id: str
    :param idempotency_key: A API suporta idempotência para que, após um erro de conexão, por exemplo, se possa tentar novamente requisições POST sem acidentalmente efetuar a mesma operação duas vezes. Para indicar uma requisição é idempotente, envie uma IdempotencyKey no header da requisição com uma chave única (recomendamos UUIDs V4).
    :type idempotency_key: 

    :rtype: CreditCreatedSuccessfully
    """
    if connexion.request.is_json:
        body = NewCreditRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_credits_by_account(account_id, limit=None, starting_after=None, ending_before=None):  # noqa: E501
    """Lista cargas de créditos agendadas mas ainda não executadas.

     # noqa: E501

    :param account_id: Identificador da conta.
    :type account_id: str
    :param limit: Número limite de objetos retornados. O valor deve ser entre 1 e 100.
    :type limit: int
    :param starting_after: Um cursor para uso em paginação. {starting_after} é o identificador único do objeto a partir do qual se quer listar. Por exemplo, se houve um retorno de uma lista de 100 objetos para esta chamada sendo que o último possui identificador \&quot;obj1234\&quot;, para se obter a página use \&quot;starting_after&#x3D;obj1234\&quot;.
    :type starting_after: str
    :param ending_before: Um cursor para uso em paginação. {ending_before} é o identificador único do objeto a partir do qual se quer listar os anteriores. Por exemplo, se houve um retorno de uma lista de 100 objetos para esta chamada sendo que o primeiro possui identificador \&quot;obj1234\&quot;, para se obter a página anterior use \&quot;ending_before&#x3D;obj1234\&quot;.
    :type ending_before: str

    :rtype: CreditListResult
    """
    return 'do some magic!'


def find_transactions(limit=None, starting_after=None, ending_before=None, beginning_date_time=None, ending_date_time=None, transaction_type=None, transaction_status=None, transaction_approved=None, transaction_denial_code=None, minimum_amount=None, max_amount=None, transaction_mode=None):  # noqa: E501
    """Lista transações a partir de filtros especificados.

     # noqa: E501

    :param limit: Número limite de objetos retornados. O valor deve ser entre 1 e 100.
    :type limit: int
    :param starting_after: Um cursor para uso em paginação. {starting_after} é o identificador único do objeto a partir do qual se quer listar. Por exemplo, se houve um retorno de uma lista de 100 objetos para esta chamada sendo que o último possui identificador \&quot;obj1234\&quot;, para se obter a página use \&quot;starting_after&#x3D;obj1234\&quot;.
    :type starting_after: str
    :param ending_before: Um cursor para uso em paginação. {ending_before} é o identificador único do objeto a partir do qual se quer listar os anteriores. Por exemplo, se houve um retorno de uma lista de 100 objetos para esta chamada sendo que o primeiro possui identificador \&quot;obj1234\&quot;, para se obter a página anterior use \&quot;ending_before&#x3D;obj1234\&quot;.
    :type ending_before: str
    :param beginning_date_time: Data e hora para iniciar procura.
    :type beginning_date_time: str
    :param ending_date_time: Data e hora para parar procura.
    :type ending_date_time: str
    :param transaction_type: Tipo das transações a serem retornadas.
    :type transaction_type: dict | bytes
    :param transaction_status: Status das transações a serem retornadas.
    :type transaction_status: dict | bytes
    :param transaction_approved: Se a transação foi aprovada pelo autorizador.
    :type transaction_approved: bool
    :param transaction_denial_code: Transações negadas no autorizador com um código específico.
    :type transaction_denial_code: str
    :param minimum_amount: Valor mínimo, omitindo a vírgula. Por exemplo, R$ 1,23 ficaria \&quot;amount\&quot;:123
    :type minimum_amount: int
    :param max_amount: Valor máximo, omitindo a vírgula. Por exemplo, R$ 1,23 ficaria \&quot;amount\&quot;:123
    :type max_amount: int
    :param transaction_mode: Modo da transação.
    :type transaction_mode: dict | bytes

    :rtype: TransactionListResult
    """
    beginning_date_time = util.deserialize_datetime(beginning_date_time)
    ending_date_time = util.deserialize_datetime(ending_date_time)
    if connexion.request.is_json:
        transaction_type = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        transaction_status = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        transaction_mode = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_transactions_by_account(account_id, limit=None, starting_after=None, ending_before=None, beginning_date_time=None, ending_date_time=None, transaction_type=None, transaction_status=None, transaction_approved=None, transaction_denial_code=None, minimum_amount=None, max_amount=None, transaction_mode=None):  # noqa: E501
    """Lista transações a partir de filtros especificados.

     # noqa: E501

    :param account_id: Identificador da conta.
    :type account_id: str
    :param limit: Número limite de objetos retornados. O valor deve ser entre 1 e 100.
    :type limit: int
    :param starting_after: Um cursor para uso em paginação. {starting_after} é o identificador único do objeto a partir do qual se quer listar. Por exemplo, se houve um retorno de uma lista de 100 objetos para esta chamada sendo que o último possui identificador \&quot;obj1234\&quot;, para se obter a página use \&quot;starting_after&#x3D;obj1234\&quot;.
    :type starting_after: str
    :param ending_before: Um cursor para uso em paginação. {ending_before} é o identificador único do objeto a partir do qual se quer listar os anteriores. Por exemplo, se houve um retorno de uma lista de 100 objetos para esta chamada sendo que o primeiro possui identificador \&quot;obj1234\&quot;, para se obter a página anterior use \&quot;ending_before&#x3D;obj1234\&quot;.
    :type ending_before: str
    :param beginning_date_time: Data e hora para iniciar procura.
    :type beginning_date_time: str
    :param ending_date_time: Data e hora para parar procura.
    :type ending_date_time: str
    :param transaction_type: Tipo das transações a serem retornadas.
    :type transaction_type: dict | bytes
    :param transaction_status: Status das transações a serem retornadas.
    :type transaction_status: dict | bytes
    :param transaction_approved: Se a transação foi aprovada pelo autorizador.
    :type transaction_approved: bool
    :param transaction_denial_code: Transações negadas no autorizador com um código específico.
    :type transaction_denial_code: str
    :param minimum_amount: Valor mínimo, omitindo a vírgula. Por exemplo, R$ 1,23 ficaria \&quot;amount\&quot;:123
    :type minimum_amount: int
    :param max_amount: Valor máximo, omitindo a vírgula. Por exemplo, R$ 1,23 ficaria \&quot;amount\&quot;:123
    :type max_amount: int
    :param transaction_mode: Modo da transação.
    :type transaction_mode: dict | bytes

    :rtype: TransactionListResult
    """
    beginning_date_time = util.deserialize_datetime(beginning_date_time)
    ending_date_time = util.deserialize_datetime(ending_date_time)
    if connexion.request.is_json:
        transaction_type = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        transaction_status = .from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        transaction_mode = .from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_transaction(transaction_id):  # noqa: E501
    """Recupera informações sobre uma transação.

    Em uma operação de atendimento ao portador, essa função pode ser utilizada para retornar detalhes da transação. # noqa: E501

    :param transaction_id: Identificador da transação.
    :type transaction_id: str

    :rtype: Transaction
    """
    return 'do some magic!'
