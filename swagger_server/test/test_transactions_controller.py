# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.credit_created_successfully import CreditCreatedSuccessfully  # noqa: E501
from swagger_server.models.credit_list_result import CreditListResult  # noqa: E501
from swagger_server.models.entry_mode import EntryMode  # noqa: E501
from swagger_server.models.new_credit_request import NewCreditRequest  # noqa: E501
from swagger_server.models.result_data import ResultData  # noqa: E501
from swagger_server.models.transaction import Transaction  # noqa: E501
from swagger_server.models.transaction_list_result import TransactionListResult  # noqa: E501
from swagger_server.models.transaction_status import TransactionStatus  # noqa: E501
from swagger_server.models.transaction_type import TransactionType  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTransactionsController(BaseTestCase):
    """TransactionsController integration test stubs"""

    def test_add_credit(self):
        """Test case for add_credit

        Registra uma nova carga de créditos com data de efetivação.
        """
        body = NewCreditRequest()
        headers = [('idempotency_key', '38400000-8cf0-11bd-b23e-10b96e4ef00d')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/accounts/{accountId}/transactions/credits'.format(account_id='account_id_example'),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_credits_by_account(self):
        """Test case for find_credits_by_account

        Lista cargas de créditos agendadas mas ainda não executadas.
        """
        query_string = [('limit', 100),
                        ('starting_after', 'starting_after_example'),
                        ('ending_before', 'ending_before_example')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/accounts/{accountId}/transactions/credits'.format(account_id='account_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_transactions(self):
        """Test case for find_transactions

        Lista transações a partir de filtros especificados.
        """
        query_string = [('limit', 100),
                        ('starting_after', 'starting_after_example'),
                        ('ending_before', 'ending_before_example'),
                        ('beginning_date_time', '2013-10-20T19:20:30+01:00'),
                        ('ending_date_time', '2013-10-20T19:20:30+01:00'),
                        ('transaction_type', TransactionType()),
                        ('transaction_status', TransactionStatus()),
                        ('transaction_approved', true),
                        ('transaction_denial_code', 'transaction_denial_code_example'),
                        ('minimum_amount', 789),
                        ('max_amount', 789),
                        ('transaction_mode', EntryMode())]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/transactions',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_transactions_by_account(self):
        """Test case for find_transactions_by_account

        Lista transações a partir de filtros especificados.
        """
        query_string = [('limit', 100),
                        ('starting_after', 'starting_after_example'),
                        ('ending_before', 'ending_before_example'),
                        ('beginning_date_time', '2013-10-20T19:20:30+01:00'),
                        ('ending_date_time', '2013-10-20T19:20:30+01:00'),
                        ('transaction_type', TransactionType()),
                        ('transaction_status', TransactionStatus()),
                        ('transaction_approved', true),
                        ('transaction_denial_code', 'transaction_denial_code_example'),
                        ('minimum_amount', 789),
                        ('max_amount', 789),
                        ('transaction_mode', EntryMode())]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/accounts/{accountId}/transactions'.format(account_id='account_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_transaction(self):
        """Test case for get_transaction

        Recupera informações sobre uma transação.
        """
        response = self.client.open(
            '/paySmart/ps-processadora/v1/transactions/{transactionId}'.format(transaction_id='transaction_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
