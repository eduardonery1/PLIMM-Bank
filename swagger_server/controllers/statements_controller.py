import connexion
import six

from swagger_server.models.future_statement_list import FutureStatementList  # noqa: E501
from swagger_server.models.installment_options import InstallmentOptions  # noqa: E501
from swagger_server.models.installment_request import InstallmentRequest  # noqa: E501
from swagger_server.models.open_statement import OpenStatement  # noqa: E501
from swagger_server.models.result_data import ResultData  # noqa: E501
from swagger_server.models.statement import Statement  # noqa: E501
from swagger_server.models.statement_list import StatementList  # noqa: E501
from swagger_server import util


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
