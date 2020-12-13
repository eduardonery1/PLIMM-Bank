# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server import util


class DisputeEvent(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, sent_from: str=None, date_sent: Object=None, description: str=None):  # noqa: E501
        """DisputeEvent - a model defined in Swagger

        :param sent_from: The sent_from of this DisputeEvent.  # noqa: E501
        :type sent_from: str
        :param date_sent: The date_sent of this DisputeEvent.  # noqa: E501
        :type date_sent: Object
        :param description: The description of this DisputeEvent.  # noqa: E501
        :type description: str
        """
        self.swagger_types = {
            'sent_from': str,
            'date_sent': Object,
            'description': str
        }

        self.attribute_map = {
            'sent_from': 'sent_from',
            'date_sent': 'date_sent',
            'description': 'description'
        }
        self._sent_from = sent_from
        self._date_sent = date_sent
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'DisputeEvent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DisputeEvent of this DisputeEvent.  # noqa: E501
        :rtype: DisputeEvent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sent_from(self) -> str:
        """Gets the sent_from of this DisputeEvent.

        Criador do evento.  # noqa: E501

        :return: The sent_from of this DisputeEvent.
        :rtype: str
        """
        return self._sent_from

    @sent_from.setter
    def sent_from(self, sent_from: str):
        """Sets the sent_from of this DisputeEvent.

        Criador do evento.  # noqa: E501

        :param sent_from: The sent_from of this DisputeEvent.
        :type sent_from: str
        """
        allowed_values = ["issuer", "acquirer", "brand"]  # noqa: E501
        if sent_from not in allowed_values:
            raise ValueError(
                "Invalid value for `sent_from` ({0}), must be one of {1}"
                .format(sent_from, allowed_values)
            )

        self._sent_from = sent_from

    @property
    def date_sent(self) -> Object:
        """Gets the date_sent of this DisputeEvent.

        Data que o evento ocorreu.  # noqa: E501

        :return: The date_sent of this DisputeEvent.
        :rtype: Object
        """
        return self._date_sent

    @date_sent.setter
    def date_sent(self, date_sent: Object):
        """Sets the date_sent of this DisputeEvent.

        Data que o evento ocorreu.  # noqa: E501

        :param date_sent: The date_sent of this DisputeEvent.
        :type date_sent: Object
        """

        self._date_sent = date_sent

    @property
    def description(self) -> str:
        """Gets the description of this DisputeEvent.

        Descrição do evento/resposta.  # noqa: E501

        :return: The description of this DisputeEvent.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this DisputeEvent.

        Descrição do evento/resposta.  # noqa: E501

        :param description: The description of this DisputeEvent.
        :type description: str
        """

        self._description = description