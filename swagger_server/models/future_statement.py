# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server.models.source_audit import SourceAudit  # noqa: F401,E501
from swagger_server.models.statement_entry import StatementEntry  # noqa: F401,E501
from swagger_server import util


class FutureStatement(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, account_id: str=None, payment_due: str=None, close_date: str=None, balance: AllOfFutureStatementBalance=None, transactions_list: List[StatementEntry]=None, query_date: datetime=None, source_audit: SourceAudit=None):  # noqa: E501
        """FutureStatement - a model defined in Swagger

        :param account_id: The account_id of this FutureStatement.  # noqa: E501
        :type account_id: str
        :param payment_due: The payment_due of this FutureStatement.  # noqa: E501
        :type payment_due: str
        :param close_date: The close_date of this FutureStatement.  # noqa: E501
        :type close_date: str
        :param balance: The balance of this FutureStatement.  # noqa: E501
        :type balance: AllOfFutureStatementBalance
        :param transactions_list: The transactions_list of this FutureStatement.  # noqa: E501
        :type transactions_list: List[StatementEntry]
        :param query_date: The query_date of this FutureStatement.  # noqa: E501
        :type query_date: datetime
        :param source_audit: The source_audit of this FutureStatement.  # noqa: E501
        :type source_audit: SourceAudit
        """
        self.swagger_types = {
            'account_id': str,
            'payment_due': str,
            'close_date': str,
            'balance': AllOfFutureStatementBalance,
            'transactions_list': List[StatementEntry],
            'query_date': datetime,
            'source_audit': SourceAudit
        }

        self.attribute_map = {
            'account_id': 'accountId',
            'payment_due': 'paymentDue',
            'close_date': 'closeDate',
            'balance': 'balance',
            'transactions_list': 'transactionsList',
            'query_date': 'query_date',
            'source_audit': 'sourceAudit'
        }
        self._account_id = account_id
        self._payment_due = payment_due
        self._close_date = close_date
        self._balance = balance
        self._transactions_list = transactions_list
        self._query_date = query_date
        self._source_audit = source_audit

    @classmethod
    def from_dict(cls, dikt) -> 'FutureStatement':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FutureStatement of this FutureStatement.  # noqa: E501
        :rtype: FutureStatement
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account_id(self) -> str:
        """Gets the account_id of this FutureStatement.

        Identificador único da conta.  # noqa: E501

        :return: The account_id of this FutureStatement.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id: str):
        """Sets the account_id of this FutureStatement.

        Identificador único da conta.  # noqa: E501

        :param account_id: The account_id of this FutureStatement.
        :type account_id: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def payment_due(self) -> str:
        """Gets the payment_due of this FutureStatement.

        Data de vencimento da fatura.  # noqa: E501

        :return: The payment_due of this FutureStatement.
        :rtype: str
        """
        return self._payment_due

    @payment_due.setter
    def payment_due(self, payment_due: str):
        """Sets the payment_due of this FutureStatement.

        Data de vencimento da fatura.  # noqa: E501

        :param payment_due: The payment_due of this FutureStatement.
        :type payment_due: str
        """
        if payment_due is None:
            raise ValueError("Invalid value for `payment_due`, must not be `None`")  # noqa: E501

        self._payment_due = payment_due

    @property
    def close_date(self) -> str:
        """Gets the close_date of this FutureStatement.

        Data de fechamento da fatura.  # noqa: E501

        :return: The close_date of this FutureStatement.
        :rtype: str
        """
        return self._close_date

    @close_date.setter
    def close_date(self, close_date: str):
        """Sets the close_date of this FutureStatement.

        Data de fechamento da fatura.  # noqa: E501

        :param close_date: The close_date of this FutureStatement.
        :type close_date: str
        """

        self._close_date = close_date

    @property
    def balance(self) -> AllOfFutureStatementBalance:
        """Gets the balance of this FutureStatement.

        Saldo total da fatura  # noqa: E501

        :return: The balance of this FutureStatement.
        :rtype: AllOfFutureStatementBalance
        """
        return self._balance

    @balance.setter
    def balance(self, balance: AllOfFutureStatementBalance):
        """Sets the balance of this FutureStatement.

        Saldo total da fatura  # noqa: E501

        :param balance: The balance of this FutureStatement.
        :type balance: AllOfFutureStatementBalance
        """
        if balance is None:
            raise ValueError("Invalid value for `balance`, must not be `None`")  # noqa: E501

        self._balance = balance

    @property
    def transactions_list(self) -> List[StatementEntry]:
        """Gets the transactions_list of this FutureStatement.

        Lista de lançamentos em aberto  # noqa: E501

        :return: The transactions_list of this FutureStatement.
        :rtype: List[StatementEntry]
        """
        return self._transactions_list

    @transactions_list.setter
    def transactions_list(self, transactions_list: List[StatementEntry]):
        """Sets the transactions_list of this FutureStatement.

        Lista de lançamentos em aberto  # noqa: E501

        :param transactions_list: The transactions_list of this FutureStatement.
        :type transactions_list: List[StatementEntry]
        """
        if transactions_list is None:
            raise ValueError("Invalid value for `transactions_list`, must not be `None`")  # noqa: E501

        self._transactions_list = transactions_list

    @property
    def query_date(self) -> datetime:
        """Gets the query_date of this FutureStatement.

        Data de consulta.  # noqa: E501

        :return: The query_date of this FutureStatement.
        :rtype: datetime
        """
        return self._query_date

    @query_date.setter
    def query_date(self, query_date: datetime):
        """Sets the query_date of this FutureStatement.

        Data de consulta.  # noqa: E501

        :param query_date: The query_date of this FutureStatement.
        :type query_date: datetime
        """

        self._query_date = query_date

    @property
    def source_audit(self) -> SourceAudit:
        """Gets the source_audit of this FutureStatement.


        :return: The source_audit of this FutureStatement.
        :rtype: SourceAudit
        """
        return self._source_audit

    @source_audit.setter
    def source_audit(self, source_audit: SourceAudit):
        """Sets the source_audit of this FutureStatement.


        :param source_audit: The source_audit of this FutureStatement.
        :type source_audit: SourceAudit
        """

        self._source_audit = source_audit