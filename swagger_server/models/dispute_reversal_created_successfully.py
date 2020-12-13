# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.dispute import Dispute  # noqa: F401,E501
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server import util


class DisputeReversalCreatedSuccessfully(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, result_data: AllOfDisputeReversalCreatedSuccessfullyResultData=None, dispute: Dispute=None):  # noqa: E501
        """DisputeReversalCreatedSuccessfully - a model defined in Swagger

        :param result_data: The result_data of this DisputeReversalCreatedSuccessfully.  # noqa: E501
        :type result_data: AllOfDisputeReversalCreatedSuccessfullyResultData
        :param dispute: The dispute of this DisputeReversalCreatedSuccessfully.  # noqa: E501
        :type dispute: Dispute
        """
        self.swagger_types = {
            'result_data': AllOfDisputeReversalCreatedSuccessfullyResultData,
            'dispute': Dispute
        }

        self.attribute_map = {
            'result_data': 'resultData',
            'dispute': 'dispute'
        }
        self._result_data = result_data
        self._dispute = dispute

    @classmethod
    def from_dict(cls, dikt) -> 'DisputeReversalCreatedSuccessfully':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DisputeReversalCreatedSuccessfully of this DisputeReversalCreatedSuccessfully.  # noqa: E501
        :rtype: DisputeReversalCreatedSuccessfully
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result_data(self) -> AllOfDisputeReversalCreatedSuccessfullyResultData:
        """Gets the result_data of this DisputeReversalCreatedSuccessfully.


        :return: The result_data of this DisputeReversalCreatedSuccessfully.
        :rtype: AllOfDisputeReversalCreatedSuccessfullyResultData
        """
        return self._result_data

    @result_data.setter
    def result_data(self, result_data: AllOfDisputeReversalCreatedSuccessfullyResultData):
        """Sets the result_data of this DisputeReversalCreatedSuccessfully.


        :param result_data: The result_data of this DisputeReversalCreatedSuccessfully.
        :type result_data: AllOfDisputeReversalCreatedSuccessfullyResultData
        """

        self._result_data = result_data

    @property
    def dispute(self) -> Dispute:
        """Gets the dispute of this DisputeReversalCreatedSuccessfully.


        :return: The dispute of this DisputeReversalCreatedSuccessfully.
        :rtype: Dispute
        """
        return self._dispute

    @dispute.setter
    def dispute(self, dispute: Dispute):
        """Sets the dispute of this DisputeReversalCreatedSuccessfully.


        :param dispute: The dispute of this DisputeReversalCreatedSuccessfully.
        :type dispute: Dispute
        """

        self._dispute = dispute