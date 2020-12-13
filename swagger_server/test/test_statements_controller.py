# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.future_statement_list import FutureStatementList  # noqa: E501
from swagger_server.models.installment_options import InstallmentOptions  # noqa: E501
from swagger_server.models.installment_request import InstallmentRequest  # noqa: E501
from swagger_server.models.open_statement import OpenStatement  # noqa: E501
from swagger_server.models.result_data import ResultData  # noqa: E501
from swagger_server.models.statement import Statement  # noqa: E501
from swagger_server.models.statement_list import StatementList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestStatementsController(BaseTestCase):
    """StatementsController integration test stubs"""

    def test_get_account_statement_closed(self):
        """Test case for get_account_statement_closed

        Recupera informações sobre a fatura fechada mais recente para essa conta.
        """
        response = self.client.open(
            '/paySmart/ps-processadora/v1/accounts/{accountId}/statements/closed'.format(account_id='account_id_example'),
            method='GET')
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

    def test_get_account_statement_open(self):
        """Test case for get_account_statement_open

        Recupera informações sobre a fatura atualmente aberta para essa conta.
        """
        response = self.client.open(
            '/paySmart/ps-processadora/v1/accounts/{accountId}/statements/open'.format(account_id='account_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_account_statements(self):
        """Test case for get_account_statements

        Recupera informações sobre a fatura de um mês em particular. Pode ser usado para pesquisar faturas fechadas.
        """
        query_string = [('month', 'month_example')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/accounts/{accountId}/statements'.format(account_id='account_id_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_account_statements_closed(self):
        """Test case for get_account_statements_closed

        Recupera informações sobre todas as faturas que fecharam em um dia específico.
        """
        query_string = [('closing_date_query', 'closing_date_query_example')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/accounts/statements/closed',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_account_statements_future(self):
        """Test case for get_account_statements_future

        Recupera informações sobre todas as faturas futuras que já tenham algum lançamento agendado para essa conta.
        """
        response = self.client.open(
            '/paySmart/ps-processadora/v1/accounts/{accountId}/statements/future'.format(account_id='account_id_example'),
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
