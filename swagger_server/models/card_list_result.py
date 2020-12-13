# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.card import Card  # noqa: F401,E501
from swagger_server import util


class CardListResult(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, has_more: bool=None, cards: List[Card]=None):  # noqa: E501
        """CardListResult - a model defined in Swagger

        :param has_more: The has_more of this CardListResult.  # noqa: E501
        :type has_more: bool
        :param cards: The cards of this CardListResult.  # noqa: E501
        :type cards: List[Card]
        """
        self.swagger_types = {
            'has_more': bool,
            'cards': List[Card]
        }

        self.attribute_map = {
            'has_more': 'hasMore',
            'cards': 'cards'
        }
        self._has_more = has_more
        self._cards = cards

    @classmethod
    def from_dict(cls, dikt) -> 'CardListResult':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CardListResult of this CardListResult.  # noqa: E501
        :rtype: CardListResult
        """
        return util.deserialize_model(dikt, cls)

    @property
    def has_more(self) -> bool:
        """Gets the has_more of this CardListResult.

        Indica que atingiu o limite de retorno e existem mais elementos a serem retornados.  # noqa: E501

        :return: The has_more of this CardListResult.
        :rtype: bool
        """
        return self._has_more

    @has_more.setter
    def has_more(self, has_more: bool):
        """Sets the has_more of this CardListResult.

        Indica que atingiu o limite de retorno e existem mais elementos a serem retornados.  # noqa: E501

        :param has_more: The has_more of this CardListResult.
        :type has_more: bool
        """

        self._has_more = has_more

    @property
    def cards(self) -> List[Card]:
        """Gets the cards of this CardListResult.

        Lista de cartões.  # noqa: E501

        :return: The cards of this CardListResult.
        :rtype: List[Card]
        """
        return self._cards

    @cards.setter
    def cards(self, cards: List[Card]):
        """Sets the cards of this CardListResult.

        Lista de cartões.  # noqa: E501

        :param cards: The cards of this CardListResult.
        :type cards: List[Card]
        """

        self._cards = cards