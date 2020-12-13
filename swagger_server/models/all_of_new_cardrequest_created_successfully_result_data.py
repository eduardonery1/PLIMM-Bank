# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.result_data import ResultData  # noqa: F401,E501
from swagger_server import util


class AllOfNewCardrequestCreatedSuccessfullyResultData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, result_code: int=None, result_description: str=None, issuer_request_id: str=None, ps_response_id: str=None):  # noqa: E501
        """AllOfNewCardrequestCreatedSuccessfullyResultData - a model defined in Swagger

        :param result_code: The result_code of this AllOfNewCardrequestCreatedSuccessfullyResultData.  # noqa: E501
        :type result_code: int
        :param result_description: The result_description of this AllOfNewCardrequestCreatedSuccessfullyResultData.  # noqa: E501
        :type result_description: str
        :param issuer_request_id: The issuer_request_id of this AllOfNewCardrequestCreatedSuccessfullyResultData.  # noqa: E501
        :type issuer_request_id: str
        :param ps_response_id: The ps_response_id of this AllOfNewCardrequestCreatedSuccessfullyResultData.  # noqa: E501
        :type ps_response_id: str
        """
        self.swagger_types = {
            'result_code': int,
            'result_description': str,
            'issuer_request_id': str,
            'ps_response_id': str
        }

        self.attribute_map = {
            'result_code': 'resultCode',
            'result_description': 'resultDescription',
            'issuer_request_id': 'issuerRequestId',
            'ps_response_id': 'psResponseId'
        }
        self._result_code = result_code
        self._result_description = result_description
        self._issuer_request_id = issuer_request_id
        self._ps_response_id = ps_response_id

    @classmethod
    def from_dict(cls, dikt) -> 'AllOfNewCardrequestCreatedSuccessfullyResultData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AllOfNewCardrequestCreatedSuccessfullyResultData of this AllOfNewCardrequestCreatedSuccessfullyResultData.  # noqa: E501
        :rtype: AllOfNewCardrequestCreatedSuccessfullyResultData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result_code(self) -> int:
        """Gets the result_code of this AllOfNewCardrequestCreatedSuccessfullyResultData.

        Código de resultado do processamento.  # noqa: E501

        :return: The result_code of this AllOfNewCardrequestCreatedSuccessfullyResultData.
        :rtype: int
        """
        return self._result_code

    @result_code.setter
    def result_code(self, result_code: int):
        """Sets the result_code of this AllOfNewCardrequestCreatedSuccessfullyResultData.

        Código de resultado do processamento.  # noqa: E501

        :param result_code: The result_code of this AllOfNewCardrequestCreatedSuccessfullyResultData.
        :type result_code: int
        """
        if result_code is None:
            raise ValueError("Invalid value for `result_code`, must not be `None`")  # noqa: E501

        self._result_code = result_code

    @property
    def result_description(self) -> str:
        """Gets the result_description of this AllOfNewCardrequestCreatedSuccessfullyResultData.

        Descrição textual do resultado do processamento.  # noqa: E501

        :return: The result_description of this AllOfNewCardrequestCreatedSuccessfullyResultData.
        :rtype: str
        """
        return self._result_description

    @result_description.setter
    def result_description(self, result_description: str):
        """Sets the result_description of this AllOfNewCardrequestCreatedSuccessfullyResultData.

        Descrição textual do resultado do processamento.  # noqa: E501

        :param result_description: The result_description of this AllOfNewCardrequestCreatedSuccessfullyResultData.
        :type result_description: str
        """
        if result_description is None:
            raise ValueError("Invalid value for `result_description`, must not be `None`")  # noqa: E501

        self._result_description = result_description

    @property
    def issuer_request_id(self) -> str:
        """Gets the issuer_request_id of this AllOfNewCardrequestCreatedSuccessfullyResultData.

        Identificador único da requisição gerado pelo emissor. Ecoado conforme enviado na requisição.  # noqa: E501

        :return: The issuer_request_id of this AllOfNewCardrequestCreatedSuccessfullyResultData.
        :rtype: str
        """
        return self._issuer_request_id

    @issuer_request_id.setter
    def issuer_request_id(self, issuer_request_id: str):
        """Sets the issuer_request_id of this AllOfNewCardrequestCreatedSuccessfullyResultData.

        Identificador único da requisição gerado pelo emissor. Ecoado conforme enviado na requisição.  # noqa: E501

        :param issuer_request_id: The issuer_request_id of this AllOfNewCardrequestCreatedSuccessfullyResultData.
        :type issuer_request_id: str
        """

        self._issuer_request_id = issuer_request_id

    @property
    def ps_response_id(self) -> str:
        """Gets the ps_response_id of this AllOfNewCardrequestCreatedSuccessfullyResultData.

        Identificador único da resposta. Gerado pela paySmart.  # noqa: E501

        :return: The ps_response_id of this AllOfNewCardrequestCreatedSuccessfullyResultData.
        :rtype: str
        """
        return self._ps_response_id

    @ps_response_id.setter
    def ps_response_id(self, ps_response_id: str):
        """Sets the ps_response_id of this AllOfNewCardrequestCreatedSuccessfullyResultData.

        Identificador único da resposta. Gerado pela paySmart.  # noqa: E501

        :param ps_response_id: The ps_response_id of this AllOfNewCardrequestCreatedSuccessfullyResultData.
        :type ps_response_id: str
        """
        if ps_response_id is None:
            raise ValueError("Invalid value for `ps_response_id`, must not be `None`")  # noqa: E501

        self._ps_response_id = ps_response_id