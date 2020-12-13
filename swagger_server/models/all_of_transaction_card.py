# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.card import Card  # noqa: F401,E501
from swagger_server.models.card_status import CardStatus  # noqa: F401,E501
from swagger_server.models.cardholder_data import CardholderData  # noqa: F401,E501
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server import util


class AllOfTransactionCard(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, card_id: str=None, account_id: str=None, issuer_card_id: str=None, issuer_card_holder_id: str=None, bin: str=None, last4_digits: str=None, expiration_date: str=None, cardholder_data: CardholderData=None, profile: str=None, product: str=None, status: CardStatus=None, block_information: Object=None, issuance_date: str=None):  # noqa: E501
        """AllOfTransactionCard - a model defined in Swagger

        :param card_id: The card_id of this AllOfTransactionCard.  # noqa: E501
        :type card_id: str
        :param account_id: The account_id of this AllOfTransactionCard.  # noqa: E501
        :type account_id: str
        :param issuer_card_id: The issuer_card_id of this AllOfTransactionCard.  # noqa: E501
        :type issuer_card_id: str
        :param issuer_card_holder_id: The issuer_card_holder_id of this AllOfTransactionCard.  # noqa: E501
        :type issuer_card_holder_id: str
        :param bin: The bin of this AllOfTransactionCard.  # noqa: E501
        :type bin: str
        :param last4_digits: The last4_digits of this AllOfTransactionCard.  # noqa: E501
        :type last4_digits: str
        :param expiration_date: The expiration_date of this AllOfTransactionCard.  # noqa: E501
        :type expiration_date: str
        :param cardholder_data: The cardholder_data of this AllOfTransactionCard.  # noqa: E501
        :type cardholder_data: CardholderData
        :param profile: The profile of this AllOfTransactionCard.  # noqa: E501
        :type profile: str
        :param product: The product of this AllOfTransactionCard.  # noqa: E501
        :type product: str
        :param status: The status of this AllOfTransactionCard.  # noqa: E501
        :type status: CardStatus
        :param block_information: The block_information of this AllOfTransactionCard.  # noqa: E501
        :type block_information: Object
        :param issuance_date: The issuance_date of this AllOfTransactionCard.  # noqa: E501
        :type issuance_date: str
        """
        self.swagger_types = {
            'card_id': str,
            'account_id': str,
            'issuer_card_id': str,
            'issuer_card_holder_id': str,
            'bin': str,
            'last4_digits': str,
            'expiration_date': str,
            'cardholder_data': CardholderData,
            'profile': str,
            'product': str,
            'status': CardStatus,
            'block_information': Object,
            'issuance_date': str
        }

        self.attribute_map = {
            'card_id': 'cardId',
            'account_id': 'accountId',
            'issuer_card_id': 'issuerCardId',
            'issuer_card_holder_id': 'issuerCardHolderId',
            'bin': 'bin',
            'last4_digits': 'last4Digits',
            'expiration_date': 'expirationDate',
            'cardholder_data': 'cardholderData',
            'profile': 'profile',
            'product': 'product',
            'status': 'status',
            'block_information': 'blockInformation',
            'issuance_date': 'issuanceDate'
        }
        self._card_id = card_id
        self._account_id = account_id
        self._issuer_card_id = issuer_card_id
        self._issuer_card_holder_id = issuer_card_holder_id
        self._bin = bin
        self._last4_digits = last4_digits
        self._expiration_date = expiration_date
        self._cardholder_data = cardholder_data
        self._profile = profile
        self._product = product
        self._status = status
        self._block_information = block_information
        self._issuance_date = issuance_date

    @classmethod
    def from_dict(cls, dikt) -> 'AllOfTransactionCard':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AllOfTransactionCard of this AllOfTransactionCard.  # noqa: E501
        :rtype: AllOfTransactionCard
        """
        return util.deserialize_model(dikt, cls)

    @property
    def card_id(self) -> str:
        """Gets the card_id of this AllOfTransactionCard.

        Identificador único do cartão.  # noqa: E501

        :return: The card_id of this AllOfTransactionCard.
        :rtype: str
        """
        return self._card_id

    @card_id.setter
    def card_id(self, card_id: str):
        """Sets the card_id of this AllOfTransactionCard.

        Identificador único do cartão.  # noqa: E501

        :param card_id: The card_id of this AllOfTransactionCard.
        :type card_id: str
        """
        if card_id is None:
            raise ValueError("Invalid value for `card_id`, must not be `None`")  # noqa: E501

        self._card_id = card_id

    @property
    def account_id(self) -> str:
        """Gets the account_id of this AllOfTransactionCard.

        Identificador único da conta.  # noqa: E501

        :return: The account_id of this AllOfTransactionCard.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id: str):
        """Sets the account_id of this AllOfTransactionCard.

        Identificador único da conta.  # noqa: E501

        :param account_id: The account_id of this AllOfTransactionCard.
        :type account_id: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def issuer_card_id(self) -> str:
        """Gets the issuer_card_id of this AllOfTransactionCard.

        Identificador único para esse cartão no emissor.  # noqa: E501

        :return: The issuer_card_id of this AllOfTransactionCard.
        :rtype: str
        """
        return self._issuer_card_id

    @issuer_card_id.setter
    def issuer_card_id(self, issuer_card_id: str):
        """Sets the issuer_card_id of this AllOfTransactionCard.

        Identificador único para esse cartão no emissor.  # noqa: E501

        :param issuer_card_id: The issuer_card_id of this AllOfTransactionCard.
        :type issuer_card_id: str
        """

        self._issuer_card_id = issuer_card_id

    @property
    def issuer_card_holder_id(self) -> str:
        """Gets the issuer_card_holder_id of this AllOfTransactionCard.

        Identificador único para esse cartão no emissor.  # noqa: E501

        :return: The issuer_card_holder_id of this AllOfTransactionCard.
        :rtype: str
        """
        return self._issuer_card_holder_id

    @issuer_card_holder_id.setter
    def issuer_card_holder_id(self, issuer_card_holder_id: str):
        """Sets the issuer_card_holder_id of this AllOfTransactionCard.

        Identificador único para esse cartão no emissor.  # noqa: E501

        :param issuer_card_holder_id: The issuer_card_holder_id of this AllOfTransactionCard.
        :type issuer_card_holder_id: str
        """

        self._issuer_card_holder_id = issuer_card_holder_id

    @property
    def bin(self) -> str:
        """Gets the bin of this AllOfTransactionCard.

        BIN do cartão (6 a 8 dígitos).  # noqa: E501

        :return: The bin of this AllOfTransactionCard.
        :rtype: str
        """
        return self._bin

    @bin.setter
    def bin(self, bin: str):
        """Sets the bin of this AllOfTransactionCard.

        BIN do cartão (6 a 8 dígitos).  # noqa: E501

        :param bin: The bin of this AllOfTransactionCard.
        :type bin: str
        """
        if bin is None:
            raise ValueError("Invalid value for `bin`, must not be `None`")  # noqa: E501

        self._bin = bin

    @property
    def last4_digits(self) -> str:
        """Gets the last4_digits of this AllOfTransactionCard.

        Últimos 4 dígitos do cartão.  # noqa: E501

        :return: The last4_digits of this AllOfTransactionCard.
        :rtype: str
        """
        return self._last4_digits

    @last4_digits.setter
    def last4_digits(self, last4_digits: str):
        """Sets the last4_digits of this AllOfTransactionCard.

        Últimos 4 dígitos do cartão.  # noqa: E501

        :param last4_digits: The last4_digits of this AllOfTransactionCard.
        :type last4_digits: str
        """
        if last4_digits is None:
            raise ValueError("Invalid value for `last4_digits`, must not be `None`")  # noqa: E501

        self._last4_digits = last4_digits

    @property
    def expiration_date(self) -> str:
        """Gets the expiration_date of this AllOfTransactionCard.

        Data de expiração no formato MM/YYYY  # noqa: E501

        :return: The expiration_date of this AllOfTransactionCard.
        :rtype: str
        """
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date: str):
        """Sets the expiration_date of this AllOfTransactionCard.

        Data de expiração no formato MM/YYYY  # noqa: E501

        :param expiration_date: The expiration_date of this AllOfTransactionCard.
        :type expiration_date: str
        """
        if expiration_date is None:
            raise ValueError("Invalid value for `expiration_date`, must not be `None`")  # noqa: E501

        self._expiration_date = expiration_date

    @property
    def cardholder_data(self) -> CardholderData:
        """Gets the cardholder_data of this AllOfTransactionCard.


        :return: The cardholder_data of this AllOfTransactionCard.
        :rtype: CardholderData
        """
        return self._cardholder_data

    @cardholder_data.setter
    def cardholder_data(self, cardholder_data: CardholderData):
        """Sets the cardholder_data of this AllOfTransactionCard.


        :param cardholder_data: The cardholder_data of this AllOfTransactionCard.
        :type cardholder_data: CardholderData
        """
        if cardholder_data is None:
            raise ValueError("Invalid value for `cardholder_data`, must not be `None`")  # noqa: E501

        self._cardholder_data = cardholder_data

    @property
    def profile(self) -> str:
        """Gets the profile of this AllOfTransactionCard.

        Perfil do cartão EMV de pagamento.  # noqa: E501

        :return: The profile of this AllOfTransactionCard.
        :rtype: str
        """
        return self._profile

    @profile.setter
    def profile(self, profile: str):
        """Sets the profile of this AllOfTransactionCard.

        Perfil do cartão EMV de pagamento.  # noqa: E501

        :param profile: The profile of this AllOfTransactionCard.
        :type profile: str
        """
        allowed_values = ["credit", "debit", "voucher", "fleet", "combo"]  # noqa: E501
        if profile not in allowed_values:
            raise ValueError(
                "Invalid value for `profile` ({0}), must be one of {1}"
                .format(profile, allowed_values)
            )

        self._profile = profile

    @property
    def product(self) -> str:
        """Gets the product of this AllOfTransactionCard.

        Identifica o tipo de produto do emissor representado pelo cartão.  # noqa: E501

        :return: The product of this AllOfTransactionCard.
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product: str):
        """Sets the product of this AllOfTransactionCard.

        Identifica o tipo de produto do emissor representado pelo cartão.  # noqa: E501

        :param product: The product of this AllOfTransactionCard.
        :type product: str
        """
        if product is None:
            raise ValueError("Invalid value for `product`, must not be `None`")  # noqa: E501

        self._product = product

    @property
    def status(self) -> CardStatus:
        """Gets the status of this AllOfTransactionCard.


        :return: The status of this AllOfTransactionCard.
        :rtype: CardStatus
        """
        return self._status

    @status.setter
    def status(self, status: CardStatus):
        """Sets the status of this AllOfTransactionCard.


        :param status: The status of this AllOfTransactionCard.
        :type status: CardStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def block_information(self) -> Object:
        """Gets the block_information of this AllOfTransactionCard.

        Informações sobre o bloqueio do cartão. Só presente no caso de cartões bloqueados.  # noqa: E501

        :return: The block_information of this AllOfTransactionCard.
        :rtype: Object
        """
        return self._block_information

    @block_information.setter
    def block_information(self, block_information: Object):
        """Sets the block_information of this AllOfTransactionCard.

        Informações sobre o bloqueio do cartão. Só presente no caso de cartões bloqueados.  # noqa: E501

        :param block_information: The block_information of this AllOfTransactionCard.
        :type block_information: Object
        """

        self._block_information = block_information

    @property
    def issuance_date(self) -> str:
        """Gets the issuance_date of this AllOfTransactionCard.

        Data de emisão no formato dd/MM/yyyy  # noqa: E501

        :return: The issuance_date of this AllOfTransactionCard.
        :rtype: str
        """
        return self._issuance_date

    @issuance_date.setter
    def issuance_date(self, issuance_date: str):
        """Sets the issuance_date of this AllOfTransactionCard.

        Data de emisão no formato dd/MM/yyyy  # noqa: E501

        :param issuance_date: The issuance_date of this AllOfTransactionCard.
        :type issuance_date: str
        """
        if issuance_date is None:
            raise ValueError("Invalid value for `issuance_date`, must not be `None`")  # noqa: E501

        self._issuance_date = issuance_date