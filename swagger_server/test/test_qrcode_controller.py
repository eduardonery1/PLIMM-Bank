# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.bad_request_error import BadRequestError  # noqa: E501
from swagger_server.models.payment_card import PaymentCard  # noqa: E501
from swagger_server.models.payment_card_params import PaymentCardParams  # noqa: E501
from swagger_server.models.precondition_failed import PreconditionFailed  # noqa: E501
from swagger_server.models.public_key import PublicKey  # noqa: E501
from swagger_server.models.result_data import ResultData  # noqa: E501
from swagger_server.models.transaction_id import TransactionId  # noqa: E501
from swagger_server.models.unprocessed_entity import UnprocessedEntity  # noqa: E501
from swagger_server.test import BaseTestCase


class TestQrcodeController(BaseTestCase):
    """QrcodeController integration test stubs"""

    def test_get_pub_key(self):
        """Test case for get_pub_key

        Obtêm uma nova chave pública para cifrar os dados do cartão antes de enviar uma nova transação de QR Code.
        """
        response = self.client.open(
            '/paySmart/ps-processadora/v1/qrcode/publicKey',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_qrcode_payment(self):
        """Test case for qrcode_payment

        Faz um pagamento
        """
        body = PaymentCardParams()
        response = self.client.open(
            '/paySmart/ps-processadora/v1/qrcode/payment/',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
