# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CardQueryResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, bin: str=None, last_four_digits: str=None, card_id: str=None):  # noqa: E501
        """CardQueryResult - a model defined in Swagger

        :param bin: The bin of this CardQueryResult.  # noqa: E501
        :type bin: str
        :param last_four_digits: The last_four_digits of this CardQueryResult.  # noqa: E501
        :type last_four_digits: str
        :param card_id: The card_id of this CardQueryResult.  # noqa: E501
        :type card_id: str
        """
        self.swagger_types = {
            'bin': str,
            'last_four_digits': str,
            'card_id': str
        }

        self.attribute_map = {
            'bin': 'BIN',
            'last_four_digits': 'last_four_digits',
            'card_id': 'cardId'
        }
        self._bin = bin
        self._last_four_digits = last_four_digits
        self._card_id = card_id

    @classmethod
    def from_dict(cls, dikt) -> 'CardQueryResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CardQueryResult of this CardQueryResult.  # noqa: E501
        :rtype: CardQueryResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bin(self) -> str:
        """Gets the bin of this CardQueryResult.

        BIN do cartão.  # noqa: E501

        :return: The bin of this CardQueryResult.
        :rtype: str
        """
        return self._bin

    @bin.setter
    def bin(self, bin: str):
        """Sets the bin of this CardQueryResult.

        BIN do cartão.  # noqa: E501

        :param bin: The bin of this CardQueryResult.
        :type bin: str
        """

        self._bin = bin

    @property
    def last_four_digits(self) -> str:
        """Gets the last_four_digits of this CardQueryResult.

        Últimos quatro dígitos do cartão.  # noqa: E501

        :return: The last_four_digits of this CardQueryResult.
        :rtype: str
        """
        return self._last_four_digits

    @last_four_digits.setter
    def last_four_digits(self, last_four_digits: str):
        """Sets the last_four_digits of this CardQueryResult.

        Últimos quatro dígitos do cartão.  # noqa: E501

        :param last_four_digits: The last_four_digits of this CardQueryResult.
        :type last_four_digits: str
        """

        self._last_four_digits = last_four_digits

    @property
    def card_id(self) -> str:
        """Gets the card_id of this CardQueryResult.

        Identificador único do cartão.  # noqa: E501

        :return: The card_id of this CardQueryResult.
        :rtype: str
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id: str):
        """Sets the card_id of this CardQueryResult.

        Identificador único do cartão.  # noqa: E501

        :param card_id: The card_id of this CardQueryResult.
        :type card_id: str
        """

        self._card_id = card_id