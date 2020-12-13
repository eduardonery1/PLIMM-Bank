# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.account_status import AccountStatus  # noqa: F401,E501
from swagger_server.models.card import Card  # noqa: F401,E501
from swagger_server.models.credit_info import CreditInfo  # noqa: F401,E501
from swagger_server.models.object import Object  # noqa: F401,E501
from swagger_server import util


class Account(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, account_id: str=None, ps_product_code: str=None, ps_product_name: str=None, issuer_account_id: str=None, account_owner: AllOfAccountAccountOwner=None, credit_info: CreditInfo=None, cards: List[Card]=None, status: AccountStatus=None, inclusion_date: datetime=None):  # noqa: E501
        """Account - a model defined in Swagger

        :param account_id: The account_id of this Account.  # noqa: E501
        :type account_id: str
        :param ps_product_code: The ps_product_code of this Account.  # noqa: E501
        :type ps_product_code: str
        :param ps_product_name: The ps_product_name of this Account.  # noqa: E501
        :type ps_product_name: str
        :param issuer_account_id: The issuer_account_id of this Account.  # noqa: E501
        :type issuer_account_id: str
        :param account_owner: The account_owner of this Account.  # noqa: E501
        :type account_owner: AllOfAccountAccountOwner
        :param credit_info: The credit_info of this Account.  # noqa: E501
        :type credit_info: CreditInfo
        :param cards: The cards of this Account.  # noqa: E501
        :type cards: List[Card]
        :param status: The status of this Account.  # noqa: E501
        :type status: AccountStatus
        :param inclusion_date: The inclusion_date of this Account.  # noqa: E501
        :type inclusion_date: datetime
        """
        self.swagger_types = {
            'account_id': str,
            'ps_product_code': str,
            'ps_product_name': str,
            'issuer_account_id': str,
            'account_owner': AllOfAccountAccountOwner,
            'credit_info': CreditInfo,
            'cards': List[Card],
            'status': AccountStatus,
            'inclusion_date': datetime
        }

        self.attribute_map = {
            'account_id': 'accountId',
            'ps_product_code': 'psProductCode',
            'ps_product_name': 'psProductName',
            'issuer_account_id': 'issuerAccountId',
            'account_owner': 'accountOwner',
            'credit_info': 'creditInfo',
            'cards': 'cards',
            'status': 'status',
            'inclusion_date': 'inclusion_date'
        }
        self._account_id = account_id
        self._ps_product_code = ps_product_code
        self._ps_product_name = ps_product_name
        self._issuer_account_id = issuer_account_id
        self._account_owner = account_owner
        self._credit_info = credit_info
        self._cards = cards
        self._status = status
        self._inclusion_date = inclusion_date

    @classmethod
    def from_dict(cls, dikt) -> 'Account':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Account of this Account.  # noqa: E501
        :rtype: Account
        """
        return util.deserialize_model(dikt, cls)

    @property
    def account_id(self) -> str:
        """Gets the account_id of this Account.

        Identificador único da conta.  # noqa: E501

        :return: The account_id of this Account.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id: str):
        """Sets the account_id of this Account.

        Identificador único da conta.  # noqa: E501

        :param account_id: The account_id of this Account.
        :type account_id: str
        """

        self._account_id = account_id

    @property
    def ps_product_code(self) -> str:
        """Gets the ps_product_code of this Account.

        Código do produto fornecido pela paySmart.  # noqa: E501

        :return: The ps_product_code of this Account.
        :rtype: str
        """
        return self._ps_product_code

    @ps_product_code.setter
    def ps_product_code(self, ps_product_code: str):
        """Sets the ps_product_code of this Account.

        Código do produto fornecido pela paySmart.  # noqa: E501

        :param ps_product_code: The ps_product_code of this Account.
        :type ps_product_code: str
        """
        if ps_product_code is None:
            raise ValueError("Invalid value for `ps_product_code`, must not be `None`")  # noqa: E501

        self._ps_product_code = ps_product_code

    @property
    def ps_product_name(self) -> str:
        """Gets the ps_product_name of this Account.

        Nome do produto.  # noqa: E501

        :return: The ps_product_name of this Account.
        :rtype: str
        """
        return self._ps_product_name

    @ps_product_name.setter
    def ps_product_name(self, ps_product_name: str):
        """Sets the ps_product_name of this Account.

        Nome do produto.  # noqa: E501

        :param ps_product_name: The ps_product_name of this Account.
        :type ps_product_name: str
        """

        self._ps_product_name = ps_product_name

    @property
    def issuer_account_id(self) -> str:
        """Gets the issuer_account_id of this Account.

        Identificador único da conta atribuído pelo emissor.  # noqa: E501

        :return: The issuer_account_id of this Account.
        :rtype: str
        """
        return self._issuer_account_id

    @issuer_account_id.setter
    def issuer_account_id(self, issuer_account_id: str):
        """Sets the issuer_account_id of this Account.

        Identificador único da conta atribuído pelo emissor.  # noqa: E501

        :param issuer_account_id: The issuer_account_id of this Account.
        :type issuer_account_id: str
        """

        self._issuer_account_id = issuer_account_id

    @property
    def account_owner(self) -> AllOfAccountAccountOwner:
        """Gets the account_owner of this Account.

        Informações relacionadas ao titular da conta.  # noqa: E501

        :return: The account_owner of this Account.
        :rtype: AllOfAccountAccountOwner
        """
        return self._account_owner

    @account_owner.setter
    def account_owner(self, account_owner: AllOfAccountAccountOwner):
        """Sets the account_owner of this Account.

        Informações relacionadas ao titular da conta.  # noqa: E501

        :param account_owner: The account_owner of this Account.
        :type account_owner: AllOfAccountAccountOwner
        """
        if account_owner is None:
            raise ValueError("Invalid value for `account_owner`, must not be `None`")  # noqa: E501

        self._account_owner = account_owner

    @property
    def credit_info(self) -> CreditInfo:
        """Gets the credit_info of this Account.


        :return: The credit_info of this Account.
        :rtype: CreditInfo
        """
        return self._credit_info

    @credit_info.setter
    def credit_info(self, credit_info: CreditInfo):
        """Sets the credit_info of this Account.


        :param credit_info: The credit_info of this Account.
        :type credit_info: CreditInfo
        """

        self._credit_info = credit_info

    @property
    def cards(self) -> List[Card]:
        """Gets the cards of this Account.


        :return: The cards of this Account.
        :rtype: List[Card]
        """
        return self._cards

    @cards.setter
    def cards(self, cards: List[Card]):
        """Sets the cards of this Account.


        :param cards: The cards of this Account.
        :type cards: List[Card]
        """

        self._cards = cards

    @property
    def status(self) -> AccountStatus:
        """Gets the status of this Account.


        :return: The status of this Account.
        :rtype: AccountStatus
        """
        return self._status

    @status.setter
    def status(self, status: AccountStatus):
        """Sets the status of this Account.


        :param status: The status of this Account.
        :type status: AccountStatus
        """

        self._status = status

    @property
    def inclusion_date(self) -> datetime:
        """Gets the inclusion_date of this Account.

        Data de inclusão da conta.  # noqa: E501

        :return: The inclusion_date of this Account.
        :rtype: datetime
        """
        return self._inclusion_date

    @inclusion_date.setter
    def inclusion_date(self, inclusion_date: datetime):
        """Sets the inclusion_date of this Account.

        Data de inclusão da conta.  # noqa: E501

        :param inclusion_date: The inclusion_date of this Account.
        :type inclusion_date: datetime
        """

        self._inclusion_date = inclusion_date