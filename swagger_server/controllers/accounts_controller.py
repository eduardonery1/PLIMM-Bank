import connexion
import six

from swagger_server.models.account import Account  # noqa: E501
from swagger_server.models.account_balance import AccountBalance  # noqa: E501
from swagger_server.models.account_cancelled_successfully import AccountCancelledSuccessfully  # noqa: E501
from swagger_server.models.account_created_successfully import AccountCreatedSuccessfully  # noqa: E501
from swagger_server.models.account_list_result import AccountListResult  # noqa: E501
from swagger_server.models.account_status import AccountStatus  # noqa: E501
from swagger_server.models.advance_payment_request import AdvancePaymentRequest  # noqa: E501
from swagger_server.models.all_installment_purchase import AllInstallmentPurchase  # noqa: E501
from swagger_server.models.cancel_account_request import CancelAccountRequest  # noqa: E501
from swagger_server.models.credit_created_successfully import CreditCreatedSuccessfully  # noqa: E501
from swagger_server.models.credit_list_result import CreditListResult  # noqa: E501
from swagger_server.models.entry_mode import EntryMode  # noqa: E501
from swagger_server.models.future_statement_list import FutureStatementList  # noqa: E501
from swagger_server.models.installment_options import InstallmentOptions  # noqa: E501
from swagger_server.models.installment_request import InstallmentRequest  # noqa: E501
from swagger_server.models.new_account_request import NewAccountRequest  # noqa: E501
from swagger_server.models.new_card_request import NewCardRequest  # noqa: E501
from swagger_server.models.new_cardrequest_created_successfully import NewCardrequestCreatedSuccessfully  # noqa: E501
from swagger_server.models.new_credit_request import NewCreditRequest  # noqa: E501
from swagger_server.models.open_statement import OpenStatement  # noqa: E501
from swagger_server.models.result_data import ResultData  # noqa: E501
from swagger_server.models.statement import Statement  # noqa: E501
from swagger_server.models.statement_list import StatementList  # noqa: E501
from swagger_server.models.system_down_error import SystemDownError  # noqa: E501
from swagger_server.models.transaction_list_result import TransactionListResult  # noqa: E501
from swagger_server.models.transaction_status import TransactionStatus  # noqa: E501
from swagger_server.models.transaction_type import TransactionType  # noqa: E501
from swagger_server.models.update_account_request import UpdateAccountRequest  # noqa: E501
from swagger_server import util


def add_account(body, idempotency_key=None):  # noqa: E501
    """Solicita nova conta paySmart.

     # noqa: E501

    :param body: Informações relacionadas à conta, para inclusão na processadora paySmart.
    :type body: dict | bytes
    :param idempotency_key: A API suporta idempotência para que, após um erro de conexão, por exemplo, se possa tentar novamente requisições POST sem acidentalmente efetuar a mesma operação duas vezes. Para indicar uma requisição é idempotente, envie uma IdempotencyKey no header da requisição com uma chave única (recomendamos UUIDs V4).
    :type idempotency_key: 

    :rtype: AccountCreatedSuccessfully
    """
    if connexion.request.is_json:
        body = NewAccountRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


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


def cancel_account(body, account_id, idempotency_key=None):  # noqa: E501
    """Cancela uma conta e cartão(ões) associado(s).

    Solicitação de cancelamento de conta e cartão. Encerra a conta e os cartões vinculados à conta SEM EMISSÃO DE NOVA VIA DE CARTÃO. # noqa: E501

    :param body: Informações relacionadas ao cancelamento da conta.
    :type body: dict | bytes
    :param account_id: Identificador da conta.
    :type account_id: str
    :param idempotency_key: A API suporta idempotência para que, após um erro de conexão, por exemplo, se possa tentar novamente requisições POST sem acidentalmente efetuar a mesma operação duas vezes. Para indicar uma requisição é idempotente, envie uma IdempotencyKey no header da requisição com uma chave única (recomendamos UUIDs V4).
    :type idempotency_key: 

    :rtype: AccountCancelledSuccessfully
    """
    if connexion.request.is_json:
        body = CancelAccountRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_accounts(limit=None, starting_after=None, ending_before=None, identity_document_number=None, full_name=None, ps_product_code=None, account_status=None, issuer_id=None, included_since=None):  # noqa: E501
    """Lista todas as contas de um emissor de acordo com filtros estabelecidos.

     # noqa: E501

    :param limit: Número limite de objetos retornados. O valor deve ser entre 1 e 100.
    :type limit: int
    :param starting_after: Um cursor para uso em paginação. {starting_after} é o identificador único do objeto a partir do qual se quer listar. Por exemplo, se houve um retorno de uma lista de 100 objetos para esta chamada sendo que o último possui identificador \&quot;obj1234\&quot;, para se obter a página use \&quot;starting_after&#x3D;obj1234\&quot;.
    :type starting_after: str
    :param ending_before: Um cursor para uso em paginação. {ending_before} é o identificador único do objeto a partir do qual se quer listar os anteriores. Por exemplo, se houve um retorno de uma lista de 100 objetos para esta chamada sendo que o primeiro possui identificador \&quot;obj1234\&quot;, para se obter a página anterior use \&quot;ending_before&#x3D;obj1234\&quot;.
    :type ending_before: str
    :param identity_document_number: No Brasil, usar CPF ou CNPJ.
    :type identity_document_number: str
    :param full_name: Nome completo do titular.
    :type full_name: str
    :param ps_product_code: Código do produto fornecido pela paySmart.
    :type ps_product_code: str
    :param account_status: Status da conta.
    :type account_status: dict | bytes
    :param issuer_id: Identificador da conta fornecido pelo emissor na sua criação.
    :type issuer_id: str
    :param included_since: Procura contas incluídas depois dessa data.
    :type included_since: str

    :rtype: AccountListResult
    """
    if connexion.request.is_json:
        account_status = .from_dict(connexion.request.get_json())  # noqa: E501
    included_since = util.deserialize_datetime(included_since)
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


def get_account(account_id):  # noqa: E501
    """Recupera informações sobre uma conta.

    Em uma operação de atendimento ao portador, essa função pode ser utilizada para retornar detalhes da conta, a situação da conta e sua lista de cartões. # noqa: E501

    :param account_id: Identificador da conta.
    :type account_id: str

    :rtype: Account
    """
    return 'do some magic!'


def get_account_balance(account_id):  # noqa: E501
    """Recupera informações sobre o saldo e limites de uma conta.

    Retorna dados de saldo e limite da conta. Importante para mostar essas informações par o titular. # noqa: E501

    :param account_id: Identificador da conta.
    :type account_id: str

    :rtype: AccountBalance
    """
    return 'do some magic!'


def get_account_statement_closed(account_id):  # noqa: E501
    """Recupera informações sobre a fatura fechada mais recente para essa conta.

    Retorna todos os dados da fatura fechada mais recente. Uma vez que a fatura seja fechada os dados dela não mudam mais. # noqa: E501

    :param account_id: Identificador da conta.
    :type account_id: str

    :rtype: Statement
    """
    return 'do some magic!'


def get_account_statement_closed_installment_options(account_id):  # noqa: E501
    """Recupera informações sobre possibilidade de parcelamento de saldo devedor que já completou 30 dias de rotativo.

    Retorna todos os dados sobre as possibilidades de parcelamento de qualquer saldo devedor que já esteja completando 30 dias no crédito rotativo. # noqa: E501

    :param account_id: Identificador da conta.
    :type account_id: str

    :rtype: InstallmentOptions
    """
    return 'do some magic!'


def get_account_statement_open(account_id):  # noqa: E501
    """Recupera informações sobre a fatura atualmente aberta para essa conta.

    Retorna dados da fatura atualmente aberta. Até o fechamento dessa fatura ela pode continuar sendo atualizada. # noqa: E501

    :param account_id: Identificador da conta.
    :type account_id: str

    :rtype: OpenStatement
    """
    return 'do some magic!'


def get_account_statements(account_id, month):  # noqa: E501
    """Recupera informações sobre a fatura de um mês em particular. Pode ser usado para pesquisar faturas fechadas.

    Retorna todos os dados da fatura de um mês em particular. Pode ser usado para pesquisar faturas fechadas. Para acessar a fatura aberta atual, ou para verificar lançamentos em faturas futuras, é preciso usar os métodos específicos para essas faturas. # noqa: E501

    :param account_id: Identificador da conta.
    :type account_id: str
    :param month: Data indicando que um mês, no formato MM/yyyy.
    :type month: str

    :rtype: Statement
    """
    return 'do some magic!'


def get_account_statements_closed(closing_date_query=None):  # noqa: E501
    """Recupera informações sobre todas as faturas que fecharam em um dia específico.

    Retorna todos os dados das faturas que que fecharam em um dia específico, passado como parâmetro. # noqa: E501

    :param closing_date_query: Data indicando que só faturas que fecharam nessa data devem ser retornadas. No formato dd/MM/yyyy.
    :type closing_date_query: str

    :rtype: StatementList
    """
    return 'do some magic!'


def get_account_statements_future(account_id):  # noqa: E501
    """Recupera informações sobre todas as faturas futuras que já tenham algum lançamento agendado para essa conta.

    Retorna todos os dados das faturas futuras (faturas com vencimento posterior ao da fatura atualmente aberta) que tenham algum lançamento já agendado (parcelas de compras parceladas). # noqa: E501

    :param account_id: Identificador da conta.
    :type account_id: str

    :rtype: FutureStatementList
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


def request_new_card(body, account_id, idempotency_key=None):  # noqa: E501
    """Requisita um novo cartão associado a conta.

    Passa os dados necessários para o requerimento de um novo cartão associado a essa conta. O cartão pode ser par o titular ou um cartão adicional. # noqa: E501

    :param body: Dados para a requisição de novo cartão, incluindo todos os dados do portador.
    :type body: dict | bytes
    :param account_id: Identificador da conta.
    :type account_id: str
    :param idempotency_key: A API suporta idempotência para que, após um erro de conexão, por exemplo, se possa tentar novamente requisições POST sem acidentalmente efetuar a mesma operação duas vezes. Para indicar uma requisição é idempotente, envie uma IdempotencyKey no header da requisição com uma chave única (recomendamos UUIDs V4).
    :type idempotency_key: 

    :rtype: NewCardrequestCreatedSuccessfully
    """
    if connexion.request.is_json:
        body = NewCardRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_account(body, account_id):  # noqa: E501
    """Atualiza informações de conta.

    implementar # noqa: E501

    :param body: Informações relacionadas à conta e produto para atualização na processadora paySmart.
    :type body: dict | bytes
    :param account_id: Identificador da conta.
    :type account_id: str

    :rtype: Account
    """
    if connexion.request.is_json:
        body = UpdateAccountRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
