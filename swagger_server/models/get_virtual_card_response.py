# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server import util


class GetVirtualCardResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, result_data: AllOfGetVirtualCardResponseResultData=None, virtual: AllOfGetVirtualCardResponseVirtual=None, constraints: AllOfGetVirtualCardResponseConstraints=None, info: AllOfGetVirtualCardResponseInfo=None):  # noqa: E501
        """GetVirtualCardResponse - a model defined in Swagger

        :param result_data: The result_data of this GetVirtualCardResponse.  # noqa: E501
        :type result_data: AllOfGetVirtualCardResponseResultData
        :param virtual: The virtual of this GetVirtualCardResponse.  # noqa: E501
        :type virtual: AllOfGetVirtualCardResponseVirtual
        :param constraints: The constraints of this GetVirtualCardResponse.  # noqa: E501
        :type constraints: AllOfGetVirtualCardResponseConstraints
        :param info: The info of this GetVirtualCardResponse.  # noqa: E501
        :type info: AllOfGetVirtualCardResponseInfo
        """
        self.swagger_types = {
            'result_data': AllOfGetVirtualCardResponseResultData,
            'virtual': AllOfGetVirtualCardResponseVirtual,
            'constraints': AllOfGetVirtualCardResponseConstraints,
            'info': AllOfGetVirtualCardResponseInfo
        }

        self.attribute_map = {
            'result_data': 'resultData',
            'virtual': 'virtual',
            'constraints': 'constraints',
            'info': 'info'
        }
        self._result_data = result_data
        self._virtual = virtual
        self._constraints = constraints
        self._info = info

    @classmethod
    def from_dict(cls, dikt) -> 'GetVirtualCardResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GetVirtualCardResponse of this GetVirtualCardResponse.  # noqa: E501
        :rtype: GetVirtualCardResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result_data(self) -> AllOfGetVirtualCardResponseResultData:
        """Gets the result_data of this GetVirtualCardResponse.


        :return: The result_data of this GetVirtualCardResponse.
        :rtype: AllOfGetVirtualCardResponseResultData
        """
        return self._result_data

    @result_data.setter
    def result_data(self, result_data: AllOfGetVirtualCardResponseResultData):
        """Sets the result_data of this GetVirtualCardResponse.


        :param result_data: The result_data of this GetVirtualCardResponse.
        :type result_data: AllOfGetVirtualCardResponseResultData
        """

        self._result_data = result_data

    @property
    def virtual(self) -> AllOfGetVirtualCardResponseVirtual:
        """Gets the virtual of this GetVirtualCardResponse.


        :return: The virtual of this GetVirtualCardResponse.
        :rtype: AllOfGetVirtualCardResponseVirtual
        """
        return self._virtual

    @virtual.setter
    def virtual(self, virtual: AllOfGetVirtualCardResponseVirtual):
        """Sets the virtual of this GetVirtualCardResponse.


        :param virtual: The virtual of this GetVirtualCardResponse.
        :type virtual: AllOfGetVirtualCardResponseVirtual
        """

        self._virtual = virtual

    @property
    def constraints(self) -> AllOfGetVirtualCardResponseConstraints:
        """Gets the constraints of this GetVirtualCardResponse.


        :return: The constraints of this GetVirtualCardResponse.
        :rtype: AllOfGetVirtualCardResponseConstraints
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints: AllOfGetVirtualCardResponseConstraints):
        """Sets the constraints of this GetVirtualCardResponse.


        :param constraints: The constraints of this GetVirtualCardResponse.
        :type constraints: AllOfGetVirtualCardResponseConstraints
        """

        self._constraints = constraints

    @property
    def info(self) -> AllOfGetVirtualCardResponseInfo:
        """Gets the info of this GetVirtualCardResponse.


        :return: The info of this GetVirtualCardResponse.
        :rtype: AllOfGetVirtualCardResponseInfo
        """
        return self._info

    @info.setter
    def info(self, info: AllOfGetVirtualCardResponseInfo):
        """Sets the info of this GetVirtualCardResponse.


        :param info: The info of this GetVirtualCardResponse.
        :type info: AllOfGetVirtualCardResponseInfo
        """

        self._info = info