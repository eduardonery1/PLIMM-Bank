# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.balance import Balance  # noqa: E501
from swagger_server.models.credit_list_mattress import CreditListMattress  # noqa: E501
from swagger_server.models.result_data import ResultData  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDynamicProvisioningAccountController(BaseTestCase):
    """DynamicProvisioningAccountController integration test stubs"""

    def test_get_balance(self):
        """Test case for get_balance

        Solicita informação de saldo na conta colchão.
        """
        response = self.client.open(
            '/paySmart/ps-processadora/v1/dynamicProvisioningAccount/balance',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_credits(self):
        """Test case for get_credits

        Obtém uma lista de aportes realizados nos dias especificados.
        """
        query_string = [('beginning_date', 'beginning_date_example'),
                        ('end_date', 'end_date_example')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/dynamicProvisioningAccount/balance/credits',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
