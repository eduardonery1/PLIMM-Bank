# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server import util


class Credit(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, credit_id: str=None, inclusion_date: datetime=None, amount: AllOfCreditAmount=None, credit_type: int=None):  # noqa: E501
        """Credit - a model defined in Swagger

        :param credit_id: The credit_id of this Credit.  # noqa: E501
        :type credit_id: str
        :param inclusion_date: The inclusion_date of this Credit.  # noqa: E501
        :type inclusion_date: datetime
        :param amount: The amount of this Credit.  # noqa: E501
        :type amount: AllOfCreditAmount
        :param credit_type: The credit_type of this Credit.  # noqa: E501
        :type credit_type: int
        """
        self.swagger_types = {
            'credit_id': str,
            'inclusion_date': datetime,
            'amount': AllOfCreditAmount,
            'credit_type': int
        }

        self.attribute_map = {
            'credit_id': 'creditId',
            'inclusion_date': 'inclusion_date',
            'amount': 'amount',
            'credit_type': 'credit_type'
        }
        self._credit_id = credit_id
        self._inclusion_date = inclusion_date
        self._amount = amount
        self._credit_type = credit_type

    @classmethod
    def from_dict(cls, dikt) -> 'Credit':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Credit of this Credit.  # noqa: E501
        :rtype: Credit
        """
        return util.deserialize_model(dikt, cls)

    @property
    def credit_id(self) -> str:
        """Gets the credit_id of this Credit.

        Identificador da carga de créditos.  # noqa: E501

        :return: The credit_id of this Credit.
        :rtype: str
        """
        return self._credit_id

    @credit_id.setter
    def credit_id(self, credit_id: str):
        """Sets the credit_id of this Credit.

        Identificador da carga de créditos.  # noqa: E501

        :param credit_id: The credit_id of this Credit.
        :type credit_id: str
        """
        if credit_id is None:
            raise ValueError("Invalid value for `credit_id`, must not be `None`")  # noqa: E501

        self._credit_id = credit_id

    @property
    def inclusion_date(self) -> datetime:
        """Gets the inclusion_date of this Credit.

        Data de início de validade/disponibilização de crédito nos cartões.  # noqa: E501

        :return: The inclusion_date of this Credit.
        :rtype: datetime
        """
        return self._inclusion_date

    @inclusion_date.setter
    def inclusion_date(self, inclusion_date: datetime):
        """Sets the inclusion_date of this Credit.

        Data de início de validade/disponibilização de crédito nos cartões.  # noqa: E501

        :param inclusion_date: The inclusion_date of this Credit.
        :type inclusion_date: datetime
        """
        if inclusion_date is None:
            raise ValueError("Invalid value for `inclusion_date`, must not be `None`")  # noqa: E501

        self._inclusion_date = inclusion_date

    @property
    def amount(self) -> AllOfCreditAmount:
        """Gets the amount of this Credit.

        Valor do crédito a ser adicionado na conta.  # noqa: E501

        :return: The amount of this Credit.
        :rtype: AllOfCreditAmount
        """
        return self._amount

    @amount.setter
    def amount(self, amount: AllOfCreditAmount):
        """Sets the amount of this Credit.

        Valor do crédito a ser adicionado na conta.  # noqa: E501

        :param amount: The amount of this Credit.
        :type amount: AllOfCreditAmount
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def credit_type(self) -> int:
        """Gets the credit_type of this Credit.

        tipo de caga de crédito realizada (normal, emergencial, etc).  # noqa: E501

        :return: The credit_type of this Credit.
        :rtype: int
        """
        return self._credit_type

    @credit_type.setter
    def credit_type(self, credit_type: int):
        """Sets the credit_type of this Credit.

        tipo de caga de crédito realizada (normal, emergencial, etc).  # noqa: E501

        :param credit_type: The credit_type of this Credit.
        :type credit_type: int
        """
        if credit_type is None:
            raise ValueError("Invalid value for `credit_type`, must not be `None`")  # noqa: E501

        self._credit_type = credit_type