# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.dispute_event import DisputeEvent  # noqa: F401,E501
from swagger_server.models.dispute_request import DisputeRequest  # noqa: F401,E501
from swagger_server.models.dispute_status import DisputeStatus  # noqa: F401,E501
from swagger_server.models.dispute_type import DisputeType  # noqa: F401,E501
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server.models.transaction import Transaction  # noqa: F401,E501
from swagger_server import util


class Dispute(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, dispute_id: str=None, dispute_request: DisputeRequest=None, dispute_date: datetime=None, dispute_max_date_response: Object=None, dispute_type: DisputeType=None, dispute_status: DisputeStatus=None, current_stage: str=None, dispute_history: List[DisputeEvent]=None, transaction: Transaction=None):  # noqa: E501
        """Dispute - a model defined in Swagger

        :param dispute_id: The dispute_id of this Dispute.  # noqa: E501
        :type dispute_id: str
        :param dispute_request: The dispute_request of this Dispute.  # noqa: E501
        :type dispute_request: DisputeRequest
        :param dispute_date: The dispute_date of this Dispute.  # noqa: E501
        :type dispute_date: datetime
        :param dispute_max_date_response: The dispute_max_date_response of this Dispute.  # noqa: E501
        :type dispute_max_date_response: Object
        :param dispute_type: The dispute_type of this Dispute.  # noqa: E501
        :type dispute_type: DisputeType
        :param dispute_status: The dispute_status of this Dispute.  # noqa: E501
        :type dispute_status: DisputeStatus
        :param current_stage: The current_stage of this Dispute.  # noqa: E501
        :type current_stage: str
        :param dispute_history: The dispute_history of this Dispute.  # noqa: E501
        :type dispute_history: List[DisputeEvent]
        :param transaction: The transaction of this Dispute.  # noqa: E501
        :type transaction: Transaction
        """
        self.swagger_types = {
            'dispute_id': str,
            'dispute_request': DisputeRequest,
            'dispute_date': datetime,
            'dispute_max_date_response': Object,
            'dispute_type': DisputeType,
            'dispute_status': DisputeStatus,
            'current_stage': str,
            'dispute_history': List[DisputeEvent],
            'transaction': Transaction
        }

        self.attribute_map = {
            'dispute_id': 'disputeId',
            'dispute_request': 'disputeRequest',
            'dispute_date': 'disputeDate',
            'dispute_max_date_response': 'disputeMaxDateResponse',
            'dispute_type': 'disputeType',
            'dispute_status': 'disputeStatus',
            'current_stage': 'currentStage',
            'dispute_history': 'dispute_history',
            'transaction': 'transaction'
        }
        self._dispute_id = dispute_id
        self._dispute_request = dispute_request
        self._dispute_date = dispute_date
        self._dispute_max_date_response = dispute_max_date_response
        self._dispute_type = dispute_type
        self._dispute_status = dispute_status
        self._current_stage = current_stage
        self._dispute_history = dispute_history
        self._transaction = transaction

    @classmethod
    def from_dict(cls, dikt) -> 'Dispute':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Dispute of this Dispute.  # noqa: E501
        :rtype: Dispute
        """
        return util.deserialize_model(dikt, cls)

    @property
    def dispute_id(self) -> str:
        """Gets the dispute_id of this Dispute.

        Identificador único da disputa na paySmart.  # noqa: E501

        :return: The dispute_id of this Dispute.
        :rtype: str
        """
        return self._dispute_id

    @dispute_id.setter
    def dispute_id(self, dispute_id: str):
        """Sets the dispute_id of this Dispute.

        Identificador único da disputa na paySmart.  # noqa: E501

        :param dispute_id: The dispute_id of this Dispute.
        :type dispute_id: str
        """

        self._dispute_id = dispute_id

    @property
    def dispute_request(self) -> DisputeRequest:
        """Gets the dispute_request of this Dispute.


        :return: The dispute_request of this Dispute.
        :rtype: DisputeRequest
        """
        return self._dispute_request

    @dispute_request.setter
    def dispute_request(self, dispute_request: DisputeRequest):
        """Sets the dispute_request of this Dispute.


        :param dispute_request: The dispute_request of this Dispute.
        :type dispute_request: DisputeRequest
        """
        if dispute_request is None:
            raise ValueError("Invalid value for `dispute_request`, must not be `None`")  # noqa: E501

        self._dispute_request = dispute_request

    @property
    def dispute_date(self) -> datetime:
        """Gets the dispute_date of this Dispute.

        Data e hora da criação da disputa no formato definido pela RFC 3339, seção 5.6.  # noqa: E501

        :return: The dispute_date of this Dispute.
        :rtype: datetime
        """
        return self._dispute_date

    @dispute_date.setter
    def dispute_date(self, dispute_date: datetime):
        """Sets the dispute_date of this Dispute.

        Data e hora da criação da disputa no formato definido pela RFC 3339, seção 5.6.  # noqa: E501

        :param dispute_date: The dispute_date of this Dispute.
        :type dispute_date: datetime
        """
        if dispute_date is None:
            raise ValueError("Invalid value for `dispute_date`, must not be `None`")  # noqa: E501

        self._dispute_date = dispute_date

    @property
    def dispute_max_date_response(self) -> Object:
        """Gets the dispute_max_date_response of this Dispute.

        Data máxima para uma resposta no formato dd/MM/yyyy  # noqa: E501

        :return: The dispute_max_date_response of this Dispute.
        :rtype: Object
        """
        return self._dispute_max_date_response

    @dispute_max_date_response.setter
    def dispute_max_date_response(self, dispute_max_date_response: Object):
        """Sets the dispute_max_date_response of this Dispute.

        Data máxima para uma resposta no formato dd/MM/yyyy  # noqa: E501

        :param dispute_max_date_response: The dispute_max_date_response of this Dispute.
        :type dispute_max_date_response: Object
        """

        self._dispute_max_date_response = dispute_max_date_response

    @property
    def dispute_type(self) -> DisputeType:
        """Gets the dispute_type of this Dispute.


        :return: The dispute_type of this Dispute.
        :rtype: DisputeType
        """
        return self._dispute_type

    @dispute_type.setter
    def dispute_type(self, dispute_type: DisputeType):
        """Sets the dispute_type of this Dispute.


        :param dispute_type: The dispute_type of this Dispute.
        :type dispute_type: DisputeType
        """
        if dispute_type is None:
            raise ValueError("Invalid value for `dispute_type`, must not be `None`")  # noqa: E501

        self._dispute_type = dispute_type

    @property
    def dispute_status(self) -> DisputeStatus:
        """Gets the dispute_status of this Dispute.


        :return: The dispute_status of this Dispute.
        :rtype: DisputeStatus
        """
        return self._dispute_status

    @dispute_status.setter
    def dispute_status(self, dispute_status: DisputeStatus):
        """Sets the dispute_status of this Dispute.


        :param dispute_status: The dispute_status of this Dispute.
        :type dispute_status: DisputeStatus
        """
        if dispute_status is None:
            raise ValueError("Invalid value for `dispute_status`, must not be `None`")  # noqa: E501

        self._dispute_status = dispute_status

    @property
    def current_stage(self) -> str:
        """Gets the current_stage of this Dispute.

        Estágio atual do processo de disputa.  # noqa: E501

        :return: The current_stage of this Dispute.
        :rtype: str
        """
        return self._current_stage

    @current_stage.setter
    def current_stage(self, current_stage: str):
        """Sets the current_stage of this Dispute.

        Estágio atual do processo de disputa.  # noqa: E501

        :param current_stage: The current_stage of this Dispute.
        :type current_stage: str
        """
        if current_stage is None:
            raise ValueError("Invalid value for `current_stage`, must not be `None`")  # noqa: E501

        self._current_stage = current_stage

    @property
    def dispute_history(self) -> List[DisputeEvent]:
        """Gets the dispute_history of this Dispute.

        Histórico de eventos nessa disputa.  # noqa: E501

        :return: The dispute_history of this Dispute.
        :rtype: List[DisputeEvent]
        """
        return self._dispute_history

    @dispute_history.setter
    def dispute_history(self, dispute_history: List[DisputeEvent]):
        """Sets the dispute_history of this Dispute.

        Histórico de eventos nessa disputa.  # noqa: E501

        :param dispute_history: The dispute_history of this Dispute.
        :type dispute_history: List[DisputeEvent]
        """

        self._dispute_history = dispute_history

    @property
    def transaction(self) -> Transaction:
        """Gets the transaction of this Dispute.


        :return: The transaction of this Dispute.
        :rtype: Transaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction: Transaction):
        """Sets the transaction of this Dispute.


        :param transaction: The transaction of this Dispute.
        :type transaction: Transaction
        """

        self._transaction = transaction