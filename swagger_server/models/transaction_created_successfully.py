# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server.models.transaction import Transaction  # noqa: F401,E501
from swagger_server import util


class TransactionCreatedSuccessfully(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, result_data: AllOfTransactionCreatedSuccessfullyResultData=None, transaction: Transaction=None):  # noqa: E501
        """TransactionCreatedSuccessfully - a model defined in Swagger

        :param result_data: The result_data of this TransactionCreatedSuccessfully.  # noqa: E501
        :type result_data: AllOfTransactionCreatedSuccessfullyResultData
        :param transaction: The transaction of this TransactionCreatedSuccessfully.  # noqa: E501
        :type transaction: Transaction
        """
        self.swagger_types = {
            'result_data': AllOfTransactionCreatedSuccessfullyResultData,
            'transaction': Transaction
        }

        self.attribute_map = {
            'result_data': 'resultData',
            'transaction': 'transaction'
        }
        self._result_data = result_data
        self._transaction = transaction

    @classmethod
    def from_dict(cls, dikt) -> 'TransactionCreatedSuccessfully':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TransactionCreatedSuccessfully of this TransactionCreatedSuccessfully.  # noqa: E501
        :rtype: TransactionCreatedSuccessfully
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result_data(self) -> AllOfTransactionCreatedSuccessfullyResultData:
        """Gets the result_data of this TransactionCreatedSuccessfully.


        :return: The result_data of this TransactionCreatedSuccessfully.
        :rtype: AllOfTransactionCreatedSuccessfullyResultData
        """
        return self._result_data

    @result_data.setter
    def result_data(self, result_data: AllOfTransactionCreatedSuccessfullyResultData):
        """Sets the result_data of this TransactionCreatedSuccessfully.


        :param result_data: The result_data of this TransactionCreatedSuccessfully.
        :type result_data: AllOfTransactionCreatedSuccessfullyResultData
        """

        self._result_data = result_data

    @property
    def transaction(self) -> Transaction:
        """Gets the transaction of this TransactionCreatedSuccessfully.


        :return: The transaction of this TransactionCreatedSuccessfully.
        :rtype: Transaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction: Transaction):
        """Sets the transaction of this TransactionCreatedSuccessfully.


        :param transaction: The transaction of this TransactionCreatedSuccessfully.
        :type transaction: Transaction
        """

        self._transaction = transaction