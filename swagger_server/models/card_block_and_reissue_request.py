# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.source_audit import SourceAudit  # noqa: F401,E501
from swagger_server import util


class CardBlockAndReissueRequest(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, issuer_card_block_id: str=None, issuer_card_id: str=None, extra_data: str=None, block_code: int=None, reason: str=None, source_audit: SourceAudit=None):  # noqa: E501
        """CardBlockAndReissueRequest - a model defined in Swagger

        :param issuer_card_block_id: The issuer_card_block_id of this CardBlockAndReissueRequest.  # noqa: E501
        :type issuer_card_block_id: str
        :param issuer_card_id: The issuer_card_id of this CardBlockAndReissueRequest.  # noqa: E501
        :type issuer_card_id: str
        :param extra_data: The extra_data of this CardBlockAndReissueRequest.  # noqa: E501
        :type extra_data: str
        :param block_code: The block_code of this CardBlockAndReissueRequest.  # noqa: E501
        :type block_code: int
        :param reason: The reason of this CardBlockAndReissueRequest.  # noqa: E501
        :type reason: str
        :param source_audit: The source_audit of this CardBlockAndReissueRequest.  # noqa: E501
        :type source_audit: SourceAudit
        """
        self.swagger_types = {
            'issuer_card_block_id': str,
            'issuer_card_id': str,
            'extra_data': str,
            'block_code': int,
            'reason': str,
            'source_audit': SourceAudit
        }

        self.attribute_map = {
            'issuer_card_block_id': 'issuerCardBlockId',
            'issuer_card_id': 'issuerCardId',
            'extra_data': 'extraData',
            'block_code': 'blockCode',
            'reason': 'reason',
            'source_audit': 'sourceAudit'
        }
        self._issuer_card_block_id = issuer_card_block_id
        self._issuer_card_id = issuer_card_id
        self._extra_data = extra_data
        self._block_code = block_code
        self._reason = reason
        self._source_audit = source_audit

    @classmethod
    def from_dict(cls, dikt) -> 'CardBlockAndReissueRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CardBlockAndReissueRequest of this CardBlockAndReissueRequest.  # noqa: E501
        :rtype: CardBlockAndReissueRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def issuer_card_block_id(self) -> str:
        """Gets the issuer_card_block_id of this CardBlockAndReissueRequest.

        Identificador único da requisição de bloqueio. Gerado pelo emissor.  # noqa: E501

        :return: The issuer_card_block_id of this CardBlockAndReissueRequest.
        :rtype: str
        """
        return self._issuer_card_block_id

    @issuer_card_block_id.setter
    def issuer_card_block_id(self, issuer_card_block_id: str):
        """Sets the issuer_card_block_id of this CardBlockAndReissueRequest.

        Identificador único da requisição de bloqueio. Gerado pelo emissor.  # noqa: E501

        :param issuer_card_block_id: The issuer_card_block_id of this CardBlockAndReissueRequest.
        :type issuer_card_block_id: str
        """

        self._issuer_card_block_id = issuer_card_block_id

    @property
    def issuer_card_id(self) -> str:
        """Gets the issuer_card_id of this CardBlockAndReissueRequest.

        Identificador do novo cartão no emissor  # noqa: E501

        :return: The issuer_card_id of this CardBlockAndReissueRequest.
        :rtype: str
        """
        return self._issuer_card_id

    @issuer_card_id.setter
    def issuer_card_id(self, issuer_card_id: str):
        """Sets the issuer_card_id of this CardBlockAndReissueRequest.

        Identificador do novo cartão no emissor  # noqa: E501

        :param issuer_card_id: The issuer_card_id of this CardBlockAndReissueRequest.
        :type issuer_card_id: str
        """

        self._issuer_card_id = issuer_card_id

    @property
    def extra_data(self) -> str:
        """Gets the extra_data of this CardBlockAndReissueRequest.

        Dados extras para o novo cartão  # noqa: E501

        :return: The extra_data of this CardBlockAndReissueRequest.
        :rtype: str
        """
        return self._extra_data

    @extra_data.setter
    def extra_data(self, extra_data: str):
        """Sets the extra_data of this CardBlockAndReissueRequest.

        Dados extras para o novo cartão  # noqa: E501

        :param extra_data: The extra_data of this CardBlockAndReissueRequest.
        :type extra_data: str
        """

        self._extra_data = extra_data

    @property
    def block_code(self) -> int:
        """Gets the block_code of this CardBlockAndReissueRequest.

        Código identificando o tipo de bloqueio.  # noqa: E501

        :return: The block_code of this CardBlockAndReissueRequest.
        :rtype: int
        """
        return self._block_code

    @block_code.setter
    def block_code(self, block_code: int):
        """Sets the block_code of this CardBlockAndReissueRequest.

        Código identificando o tipo de bloqueio.  # noqa: E501

        :param block_code: The block_code of this CardBlockAndReissueRequest.
        :type block_code: int
        """
        if block_code is None:
            raise ValueError("Invalid value for `block_code`, must not be `None`")  # noqa: E501

        self._block_code = block_code

    @property
    def reason(self) -> str:
        """Gets the reason of this CardBlockAndReissueRequest.

        Motivo do bloqueio.  # noqa: E501

        :return: The reason of this CardBlockAndReissueRequest.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason: str):
        """Sets the reason of this CardBlockAndReissueRequest.

        Motivo do bloqueio.  # noqa: E501

        :param reason: The reason of this CardBlockAndReissueRequest.
        :type reason: str
        """

        self._reason = reason

    @property
    def source_audit(self) -> SourceAudit:
        """Gets the source_audit of this CardBlockAndReissueRequest.


        :return: The source_audit of this CardBlockAndReissueRequest.
        :rtype: SourceAudit
        """
        return self._source_audit

    @source_audit.setter
    def source_audit(self, source_audit: SourceAudit):
        """Sets the source_audit of this CardBlockAndReissueRequest.


        :param source_audit: The source_audit of this CardBlockAndReissueRequest.
        :type source_audit: SourceAudit
        """

        self._source_audit = source_audit