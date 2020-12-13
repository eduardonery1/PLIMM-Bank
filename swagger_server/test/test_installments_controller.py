# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.advance_payment_request import AdvancePaymentRequest  # noqa: E501
from swagger_server.models.all_installment_purchase import AllInstallmentPurchase  # noqa: E501
from swagger_server.models.installment_options import InstallmentOptions  # noqa: E501
from swagger_server.models.installment_request import InstallmentRequest  # noqa: E501
from swagger_server.models.result_data import ResultData  # noqa: E501
from swagger_server.test import BaseTestCase


class TestInstallmentsController(BaseTestCase):
    """InstallmentsController integration test stubs"""

    def test_advance_payment(self):
        """Test case for advance_payment

        Pedido de liquidação antecipada de parcelas futuras.
        """
        body = AdvancePaymentRequest()
        headers = [('idempotency_key', '38400000-8cf0-11bd-b23e-10b96e4ef00d')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/accounts/{accountId}/installments/advancePaymentRequest'.format(account_id='account_id_example'),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_account_statement_closed_installment_options(self):
        """Test case for get_account_statement_closed_installment_options

        Recupera informações sobre possibilidade de parcelamento de saldo devedor que já completou 30 dias de rotativo.
        """
        response = self.client.open(
            '/paySmart/ps-processadora/v1/accounts/{accountId}/statements/closed/installmentOptions'.format(account_id='account_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_future_installments(self):
        """Test case for get_future_installments

        Recupera informações sobre compras parceladas que ainda tem parcelas no futuro.
        """
        response = self.client.open(
            '/paySmart/ps-processadora/v1/accounts/{accountId}/installments/future'.format(account_id='account_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_installment_request(self):
        """Test case for installment_request

        Pedido de parcelamento de saldo devedor.
        """
        body = InstallmentRequest()
        headers = [('idempotency_key', '38400000-8cf0-11bd-b23e-10b96e4ef00d')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/accounts/{accountId}/statements/closed/installmentsRequest'.format(account_id='account_id_example'),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
