import connexion
import six

from swagger_server.models.associate_anonymous_card_request import AssociateAnonymousCardRequest  # noqa: E501
from swagger_server.models.bind_card_result import BindCardResult  # noqa: E501
from swagger_server.models.card import Card  # noqa: E501
from swagger_server.models.card_block_and_reissue_request import CardBlockAndReissueRequest  # noqa: E501
from swagger_server.models.card_block_and_reissue_result import CardBlockAndReissueResult  # noqa: E501
from swagger_server.models.card_block_request import CardBlockRequest  # noqa: E501
from swagger_server.models.card_block_result import CardBlockResult  # noqa: E501
from swagger_server.models.card_list_result import CardListResult  # noqa: E501
from swagger_server.models.card_reissue_request import CardReissueRequest  # noqa: E501
from swagger_server.models.card_reissue_result import CardReissueResult  # noqa: E501
from swagger_server.models.card_single_list_result import CardSingleListResult  # noqa: E501
from swagger_server.models.card_unblock_request import CardUnblockRequest  # noqa: E501
from swagger_server.models.card_unblock_result import CardUnblockResult  # noqa: E501
from swagger_server.models.create_virtual_card_request import CreateVirtualCardRequest  # noqa: E501
from swagger_server.models.create_virtual_card_response import CreateVirtualCardResponse  # noqa: E501
from swagger_server.models.find_card_by_pan_request import FindCardByPANRequest  # noqa: E501
from swagger_server.models.list_virtual_cards_response import ListVirtualCardsResponse  # noqa: E501
from swagger_server.models.new_anonymous_card_request import NewAnonymousCardRequest  # noqa: E501
from swagger_server.models.new_anonymous_card_request_created_successfully import NewAnonymousCardRequestCreatedSuccessfully  # noqa: E501
from swagger_server.models.new_card_request import NewCardRequest  # noqa: E501
from swagger_server.models.new_cardrequest_created_successfully import NewCardrequestCreatedSuccessfully  # noqa: E501
from swagger_server.models.pin_change_created_successfully import PinChangeCreatedSuccessfully  # noqa: E501
from swagger_server.models.pin_change_request import PinChangeRequest  # noqa: E501
from swagger_server.models.result_data import ResultData  # noqa: E501
from swagger_server.models.update_card_request import UpdateCardRequest  # noqa: E501
from swagger_server import util


def bind_card_to_cardholder(body, idempotency_key=None):  # noqa: E501
    """Associa um cartão não identificado a uma portador.

    Quando emite cartões \&quot;não identificados\&quot;, o emissor pode relacionar um cartão previamente emitido com um portador por meio desta chamada. # noqa: E501

    :param body: Dados de associação do cartão ao portador. Passar o conjunto de dados de embossing do cartão (PAN + CVV + data de exp)
    :type body: dict | bytes
    :param idempotency_key: A API suporta idempotência para que, após um erro de conexão, por exemplo, se possa tentar novamente requisições POST sem acidentalmente efetuar a mesma operação duas vezes. Para indicar uma requisição é idempotente, envie uma IdempotencyKey no header da requisição com uma chave única (recomendamos UUIDs V4).
    :type idempotency_key: 

    :rtype: BindCardResult
    """
    if connexion.request.is_json:
        body = AssociateAnonymousCardRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def block_and_reissue_card(body, card_id, idempotency_key=None):  # noqa: E501
    """Bloqueia o cartão {cardId} e emite um novo cartão para o cliente.

    Atualiza a situação do cartão para bloqueado e inicia o processo de emissão de novo cartão para o cliente. # noqa: E501

    :param body: Informações para o bloqueio e reemissão.
    :type body: dict | bytes
    :param card_id: Identificador do cartão.
    :type card_id: str
    :param idempotency_key: A API suporta idempotência para que, após um erro de conexão, por exemplo, se possa tentar novamente requisições POST sem acidentalmente efetuar a mesma operação duas vezes. Para indicar uma requisição é idempotente, envie uma IdempotencyKey no header da requisição com uma chave única (recomendamos UUIDs V4).
    :type idempotency_key: 

    :rtype: CardBlockAndReissueResult
    """
    if connexion.request.is_json:
        body = CardBlockAndReissueRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def block_card(body, card_id, idempotency_key=None):  # noqa: E501
    """Bloqueia o cartão {cardId}. Não emite outro cartão.

    Atualiza a situação do cartão para bloqueado. # noqa: E501

    :param body: Informações para o bloqueio.
    :type body: dict | bytes
    :param card_id: Identificador do cartão.
    :type card_id: str
    :param idempotency_key: A API suporta idempotência para que, após um erro de conexão, por exemplo, se possa tentar novamente requisições POST sem acidentalmente efetuar a mesma operação duas vezes. Para indicar uma requisição é idempotente, envie uma IdempotencyKey no header da requisição com uma chave única (recomendamos UUIDs V4).
    :type idempotency_key: 

    :rtype: CardBlockResult
    """
    if connexion.request.is_json:
        body = CardBlockRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def change_pin(body, card_id, idempotency_key=None):  # noqa: E501
    """Requisita uma mudança do PIN do cartão {cardId}.

    Requisita a mudaça do PIN de um cartão. Mudanças do PIN offline vão ser aplicadas na próxima transação realizada que for online e na qual o cartão puder receber um script de troca de PIN na resposta. # noqa: E501

    :param body: Informações para a mudança do PIN.
    :type body: dict | bytes
    :param card_id: Identificador do cartão.
    :type card_id: str
    :param idempotency_key: A API suporta idempotência para que, após um erro de conexão, por exemplo, se possa tentar novamente requisições POST sem acidentalmente efetuar a mesma operação duas vezes. Para indicar uma requisição é idempotente, envie uma IdempotencyKey no header da requisição com uma chave única (recomendamos UUIDs V4).
    :type idempotency_key: 

    :rtype: PinChangeCreatedSuccessfully
    """
    if connexion.request.is_json:
        body = PinChangeRequest.from_dict(connexion.request.get_json())  # noqa: E501
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


def find_cards(limit=None, starting_after=None, ending_before=None, issuer_id=None, identity_document_number=None, pan_last_4_digits=None, issued_on_or_after_date=None):  # noqa: E501
    """Recupera uma lista de cartões do emissor de acordo com os filtros definidos.

     # noqa: E501

    :param limit: Número limite de objetos retornados. O valor deve ser entre 1 e 100.
    :type limit: int
    :param starting_after: Um cursor para uso em paginação. {starting_after} é o identificador único do objeto a partir do qual se quer listar. Por exemplo, se houve um retorno de uma lista de 100 objetos para esta chamada sendo que o último possui identificador \&quot;obj1234\&quot;, para se obter a página use \&quot;starting_after&#x3D;obj1234\&quot;.
    :type starting_after: str
    :param ending_before: Um cursor para uso em paginação. {ending_before} é o identificador único do objeto a partir do qual se quer listar os anteriores. Por exemplo, se houve um retorno de uma lista de 100 objetos para esta chamada sendo que o primeiro possui identificador \&quot;obj1234\&quot;, para se obter a página anterior use \&quot;ending_before&#x3D;obj1234\&quot;.
    :type ending_before: str
    :param issuer_id: Identificador do cartão fornecido pelo emissor na sua criação.
    :type issuer_id: str
    :param identity_document_number: No Brasil, usar CPF ou CNPJ.
    :type identity_document_number: str
    :param pan_last_4_digits: Últimos 4 dígitos do cartão.
    :type pan_last_4_digits: str
    :param issued_on_or_after_date: Data indicando que só cartões emitidos depois dessa data vão ser retornados
    :type issued_on_or_after_date: str

    :rtype: CardListResult
    """
    return 'do some magic!'


def find_cards_by_pan(body):  # noqa: E501
    """Recupera uma lista de cartões do emissor pelo PAN.

     # noqa: E501

    :param body: O PAN a ser procurado.
    :type body: dict | bytes

    :rtype: CardSingleListResult
    """
    if connexion.request.is_json:
        body = FindCardByPANRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_card(card_id):  # noqa: E501
    """Recupera informações de um cartão.

     # noqa: E501

    :param card_id: Identificador do cartão.
    :type card_id: str

    :rtype: Card
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


def reissue_card(body, card_id, idempotency_key=None):  # noqa: E501
    """Gera nova via do cartão para o cliente.

    Inicia o processo de emissão de nova via do cartão para o cliente. # noqa: E501

    :param body: Informações para a emissão da nova via.
    :type body: dict | bytes
    :param card_id: Identificador do cartão.
    :type card_id: str
    :param idempotency_key: A API suporta idempotência para que, após um erro de conexão, por exemplo, se possa tentar novamente requisições POST sem acidentalmente efetuar a mesma operação duas vezes. Para indicar uma requisição é idempotente, envie uma IdempotencyKey no header da requisição com uma chave única (recomendamos UUIDs V4).
    :type idempotency_key: 

    :rtype: CardReissueResult
    """
    if connexion.request.is_json:
        body = CardReissueRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def request_new_anonymous_card(body, idempotency_key=None):  # noqa: E501
    """Requisita um novo cartão \&quot;não identificado\&quot; que será associado a um usuário em um ponto futuro.

    Passa os dados necessários para o requerimento de um novo cartão que não vai estar atualmente associado a um usuário. # noqa: E501

    :param body: Dados para a requisição de novo cartão, sem dados de portador.
    :type body: dict | bytes
    :param idempotency_key: A API suporta idempotência para que, após um erro de conexão, por exemplo, se possa tentar novamente requisições POST sem acidentalmente efetuar a mesma operação duas vezes. Para indicar uma requisição é idempotente, envie uma IdempotencyKey no header da requisição com uma chave única (recomendamos UUIDs V4).
    :type idempotency_key: 

    :rtype: NewAnonymousCardRequestCreatedSuccessfully
    """
    if connexion.request.is_json:
        body = NewAnonymousCardRequest.from_dict(connexion.request.get_json())  # noqa: E501
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


def unblock_card(body, card_id, idempotency_key=None):  # noqa: E501
    """Desbloqueia o cartão {cardId}.

    Atualiza a situação do cartão para desbloqueado. # noqa: E501

    :param body: Informações para o desbloqueio.
    :type body: dict | bytes
    :param card_id: Identificador do cartão.
    :type card_id: str
    :param idempotency_key: A API suporta idempotência para que, após um erro de conexão, por exemplo, se possa tentar novamente requisições POST sem acidentalmente efetuar a mesma operação duas vezes. Para indicar uma requisição é idempotente, envie uma IdempotencyKey no header da requisição com uma chave única (recomendamos UUIDs V4).
    :type idempotency_key: 

    :rtype: CardUnblockResult
    """
    if connexion.request.is_json:
        body = CardUnblockRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_card(body, card_id):  # noqa: E501
    """Atualiza informações do cartão, permitindo vincular um portador uma única vez.

     # noqa: E501

    :param body: Informações relacionadas ao portador para atualização na processadora paySmart..
    :type body: dict | bytes
    :param card_id: Identificador do cartão.
    :type card_id: str

    :rtype: CardBlockResult
    """
    if connexion.request.is_json:
        body = UpdateCardRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
