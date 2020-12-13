# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.amount import Amount  # noqa: F401,E501
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server import util


class StatementEntry(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, transaction_id: str=None, card_id: str=None, last_four_digits: str=None, international_transaction: bool=None, transaction_date: Object=None, transaction_description: str=None, amount: Amount=None, amount_dollar: Amount=None, debit_or_credit: str=None):  # noqa: E501
        """StatementEntry - a model defined in Swagger

        :param transaction_id: The transaction_id of this StatementEntry.  # noqa: E501
        :type transaction_id: str
        :param card_id: The card_id of this StatementEntry.  # noqa: E501
        :type card_id: str
        :param last_four_digits: The last_four_digits of this StatementEntry.  # noqa: E501
        :type last_four_digits: str
        :param international_transaction: The international_transaction of this StatementEntry.  # noqa: E501
        :type international_transaction: bool
        :param transaction_date: The transaction_date of this StatementEntry.  # noqa: E501
        :type transaction_date: Object
        :param transaction_description: The transaction_description of this StatementEntry.  # noqa: E501
        :type transaction_description: str
        :param amount: The amount of this StatementEntry.  # noqa: E501
        :type amount: Amount
        :param amount_dollar: The amount_dollar of this StatementEntry.  # noqa: E501
        :type amount_dollar: Amount
        :param debit_or_credit: The debit_or_credit of this StatementEntry.  # noqa: E501
        :type debit_or_credit: str
        """
        self.swagger_types = {
            'transaction_id': str,
            'card_id': str,
            'last_four_digits': str,
            'international_transaction': bool,
            'transaction_date': Object,
            'transaction_description': str,
            'amount': Amount,
            'amount_dollar': Amount,
            'debit_or_credit': str
        }

        self.attribute_map = {
            'transaction_id': 'transactionId',
            'card_id': 'cardId',
            'last_four_digits': 'last_four_digits',
            'international_transaction': 'internationalTransaction',
            'transaction_date': 'transactionDate',
            'transaction_description': 'transactionDescription',
            'amount': 'amount',
            'amount_dollar': 'amountDollar',
            'debit_or_credit': 'debit_or_credit'
        }
        self._transaction_id = transaction_id
        self._card_id = card_id
        self._last_four_digits = last_four_digits
        self._international_transaction = international_transaction
        self._transaction_date = transaction_date
        self._transaction_description = transaction_description
        self._amount = amount
        self._amount_dollar = amount_dollar
        self._debit_or_credit = debit_or_credit

    @classmethod
    def from_dict(cls, dikt) -> 'StatementEntry':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The StatementEntry of this StatementEntry.  # noqa: E501
        :rtype: StatementEntry
        """
        return util.deserialize_model(dikt, cls)

    @property
    def transaction_id(self) -> str:
        """Gets the transaction_id of this StatementEntry.

        Identificador único da transação representada nesse lançamento.  # noqa: E501

        :return: The transaction_id of this StatementEntry.
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id: str):
        """Sets the transaction_id of this StatementEntry.

        Identificador único da transação representada nesse lançamento.  # noqa: E501

        :param transaction_id: The transaction_id of this StatementEntry.
        :type transaction_id: str
        """

        self._transaction_id = transaction_id

    @property
    def card_id(self) -> str:
        """Gets the card_id of this StatementEntry.

        Identificador único do cartão.  # noqa: E501

        :return: The card_id of this StatementEntry.
        :rtype: str
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id: str):
        """Sets the card_id of this StatementEntry.

        Identificador único do cartão.  # noqa: E501

        :param card_id: The card_id of this StatementEntry.
        :type card_id: str
        """

        self._card_id = card_id

    @property
    def last_four_digits(self) -> str:
        """Gets the last_four_digits of this StatementEntry.

        Últimos quatro dígitos do cartão.  # noqa: E501

        :return: The last_four_digits of this StatementEntry.
        :rtype: str
        """
        return self._last_four_digits

    @last_four_digits.setter
    def last_four_digits(self, last_four_digits: str):
        """Sets the last_four_digits of this StatementEntry.

        Últimos quatro dígitos do cartão.  # noqa: E501

        :param last_four_digits: The last_four_digits of this StatementEntry.
        :type last_four_digits: str
        """
        if last_four_digits is None:
            raise ValueError("Invalid value for `last_four_digits`, must not be `None`")  # noqa: E501

        self._last_four_digits = last_four_digits

    @property
    def international_transaction(self) -> bool:
        """Gets the international_transaction of this StatementEntry.

        Indica se a transação é internacional (True) ou não (False)  # noqa: E501

        :return: The international_transaction of this StatementEntry.
        :rtype: bool
        """
        return self._international_transaction

    @international_transaction.setter
    def international_transaction(self, international_transaction: bool):
        """Sets the international_transaction of this StatementEntry.

        Indica se a transação é internacional (True) ou não (False)  # noqa: E501

        :param international_transaction: The international_transaction of this StatementEntry.
        :type international_transaction: bool
        """
        if international_transaction is None:
            raise ValueError("Invalid value for `international_transaction`, must not be `None`")  # noqa: E501

        self._international_transaction = international_transaction

    @property
    def transaction_date(self) -> Object:
        """Gets the transaction_date of this StatementEntry.

        Data em que a transação ocorreu.  # noqa: E501

        :return: The transaction_date of this StatementEntry.
        :rtype: Object
        """
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date: Object):
        """Sets the transaction_date of this StatementEntry.

        Data em que a transação ocorreu.  # noqa: E501

        :param transaction_date: The transaction_date of this StatementEntry.
        :type transaction_date: Object
        """
        if transaction_date is None:
            raise ValueError("Invalid value for `transaction_date`, must not be `None`")  # noqa: E501

        self._transaction_date = transaction_date

    @property
    def transaction_description(self) -> str:
        """Gets the transaction_description of this StatementEntry.

        Descrição da transação, para ser mostrada na fatura.  # noqa: E501

        :return: The transaction_description of this StatementEntry.
        :rtype: str
        """
        return self._transaction_description

    @transaction_description.setter
    def transaction_description(self, transaction_description: str):
        """Sets the transaction_description of this StatementEntry.

        Descrição da transação, para ser mostrada na fatura.  # noqa: E501

        :param transaction_description: The transaction_description of this StatementEntry.
        :type transaction_description: str
        """
        if transaction_description is None:
            raise ValueError("Invalid value for `transaction_description`, must not be `None`")  # noqa: E501

        self._transaction_description = transaction_description

    @property
    def amount(self) -> Amount:
        """Gets the amount of this StatementEntry.


        :return: The amount of this StatementEntry.
        :rtype: Amount
        """
        return self._amount

    @amount.setter
    def amount(self, amount: Amount):
        """Sets the amount of this StatementEntry.


        :param amount: The amount of this StatementEntry.
        :type amount: Amount
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def amount_dollar(self) -> Amount:
        """Gets the amount_dollar of this StatementEntry.


        :return: The amount_dollar of this StatementEntry.
        :rtype: Amount
        """
        return self._amount_dollar

    @amount_dollar.setter
    def amount_dollar(self, amount_dollar: Amount):
        """Sets the amount_dollar of this StatementEntry.


        :param amount_dollar: The amount_dollar of this StatementEntry.
        :type amount_dollar: Amount
        """

        self._amount_dollar = amount_dollar

    @property
    def debit_or_credit(self) -> str:
        """Gets the debit_or_credit of this StatementEntry.

        Define se a transação gerou um débito ou um crédito.  # noqa: E501

        :return: The debit_or_credit of this StatementEntry.
        :rtype: str
        """
        return self._debit_or_credit

    @debit_or_credit.setter
    def debit_or_credit(self, debit_or_credit: str):
        """Sets the debit_or_credit of this StatementEntry.

        Define se a transação gerou um débito ou um crédito.  # noqa: E501

        :param debit_or_credit: The debit_or_credit of this StatementEntry.
        :type debit_or_credit: str
        """
        allowed_values = ["debit", "credit"]  # noqa: E501
        if debit_or_credit not in allowed_values:
            raise ValueError(
                "Invalid value for `debit_or_credit` ({0}), must be one of {1}"
                .format(debit_or_credit, allowed_values)
            )

        self._debit_or_credit = debit_or_credit