import connexion
import six

from swagger_server.models.bad_request_error import BadRequestError  # noqa: E501
from swagger_server.models.payment_card import PaymentCard  # noqa: E501
from swagger_server.models.payment_card_params import PaymentCardParams  # noqa: E501
from swagger_server.models.precondition_failed import PreconditionFailed  # noqa: E501
from swagger_server.models.public_key import PublicKey  # noqa: E501
from swagger_server.models.result_data import ResultData  # noqa: E501
from swagger_server.models.transaction_id import TransactionId  # noqa: E501
from swagger_server.models.unprocessed_entity import UnprocessedEntity  # noqa: E501
from swagger_server import util


def get_pub_key():  # noqa: E501
    """Obtêm uma nova chave pública para cifrar os dados do cartão antes de enviar uma nova transação de QR Code.

    Chave pública para criptografar os dados do cartão  (&#x27;cardData&#x27;: {\&quot;cardHolder\&quot;:{\&quot;card\&quot;:{\&quot;pan\&quot;:\&quot;6550001020301234\&quot;,\&quot;expiry\&quot;:{\&quot;month\&quot;:\&quot;01\&quot;,\&quot;year\&quot;:\&quot;2021\&quot;},\&quot;name\&quot;:\&quot;JOAO SILVA\&quot;,\&quot;csc\&quot;:\&quot;123\&quot;},\&quot;cpf\&quot;:\&quot;18535908005\&quot;}}) a serem enviados no pedido de pagamento. A chave é retornada junto com o tempo até a sua expiração, e pode ser utilizada mais de uma vez. É recomendado que a chave seja armazenada em back-end e sua validade seja controlada. A cifra utilizada é RSA/ECB/PKCS1Padding. A chave retornada é X509 SubjectKeyInfo no formato DER codificado em Base64. # noqa: E501


    :rtype: PublicKey
    """
    return 'do some magic!'


def qrcode_payment(body):  # noqa: E501
    """Faz um pagamento

    Solicitação de pagamento com o cartão # noqa: E501

    :param body: Informações para o pagamento
    :type body: dict | bytes

    :rtype: PaymentCard
    """
    if connexion.request.is_json:
        body = PaymentCardParams.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
