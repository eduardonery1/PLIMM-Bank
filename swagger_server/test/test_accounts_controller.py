# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

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
from swagger_server.test import BaseTestCase


class TestAccountsController(BaseTestCase):
    """AccountsController integration test stubs"""

    def test_add_account(self):
        """Test case for add_account

        Solicita nova conta paySmart.
        """
        body = NewAccountRequest()
        headers = [('idempotency_key', '38400000-8cf0-11bd-b23e-10b96e4ef00d')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/accounts',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

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

    def test_cancel_account(self):
        """Test case for cancel_account

        Cancela uma conta e cartão(ões) associado(s).
        """
        body = CancelAccountRequest()
        headers = [('idempotency_key', '38400000-8cf0-11bd-b23e-10b96e4ef00d')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/accounts/{accountId}/cancelAccount'.format(account_id='account_id_example'),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_accounts(self):
        """Test case for find_accounts

        Lista todas as contas de um emissor de acordo com filtros estabelecidos.
        """
        query_string = [('limit', 100),
                        ('starting_after', 'starting_after_example'),
                        ('ending_before', 'ending_before_example'),
                        ('identity_document_number', 'identity_document_number_example'),
                        ('full_name', 'full_name_example'),
                        ('ps_product_code', 'ps_product_code_example'),
                        ('account_status', AccountStatus()),
                        ('issuer_id', 'issuer_id_example'),
                        ('included_since', '2013-10-20T19:20:30+01:00')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/accounts',
            method='GET',
            query_string=query_string)
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

    def test_get_account(self):
        """Test case for get_account

        Recupera informações sobre uma conta.
        """
        response = self.client.open(
            '/paySmart/ps-processadora/v1/accounts/{accountId}'.format(account_id='account_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_account_balance(self):
        """Test case for get_account_balance

        Recupera informações sobre o saldo e limites de uma conta.
        """
        response = self.client.open(
            '/paySmart/ps-processadora/v1/accounts/{accountId}/balance'.format(account_id='account_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

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

    def test_request_new_card(self):
        """Test case for request_new_card

        Requisita um novo cartão associado a conta.
        """
        body = NewCardRequest()
        headers = [('idempotency_key', '38400000-8cf0-11bd-b23e-10b96e4ef00d')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/accounts/{accountId}/newCardRequest'.format(account_id='account_id_example'),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_account(self):
        """Test case for update_account

        Atualiza informações de conta.
        """
        body = UpdateAccountRequest()
        response = self.client.open(
            '/paySmart/ps-processadora/v1/accounts/{accountId}'.format(account_id='account_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
