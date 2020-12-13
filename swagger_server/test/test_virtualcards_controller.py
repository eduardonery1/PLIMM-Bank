# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.cancel_virtual_card_request import CancelVirtualCardRequest  # noqa: E501
from swagger_server.models.cancel_virtual_card_response import CancelVirtualCardResponse  # noqa: E501
from swagger_server.models.create_virtual_card_request import CreateVirtualCardRequest  # noqa: E501
from swagger_server.models.create_virtual_card_response import CreateVirtualCardResponse  # noqa: E501
from swagger_server.models.get_virtual_card_response import GetVirtualCardResponse  # noqa: E501
from swagger_server.models.list_virtual_cards_response import ListVirtualCardsResponse  # noqa: E501
from swagger_server.models.result_data import ResultData  # noqa: E501
from swagger_server.test import BaseTestCase


class TestVirtualcardsController(BaseTestCase):
    """VirtualcardsController integration test stubs"""

    def test_cancel_virtual_card(self):
        """Test case for cancel_virtual_card

        Cancela um cartão virtual.
        """
        body = CancelVirtualCardRequest()
        headers = [('idempotency_key', '38400000-8cf0-11bd-b23e-10b96e4ef00d')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/virtualcards/{vCardId}/cancel'.format(v_card_id='v_card_id_example'),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_virtual_card(self):
        """Test case for create_virtual_card

        Cria um novo cartão virtual.
        """
        body = CreateVirtualCardRequest()
        headers = [('idempotency_key', '38400000-8cf0-11bd-b23e-10b96e4ef00d')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/cards/{cardId}/virtualcards'.format(card_id='card_id_example'),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_virtual_card(self):
        """Test case for get_virtual_card

        Lista todos os cartões virtuais para um determinado cartão real
        """
        response = self.client.open(
            '/paySmart/ps-processadora/v1/virtualcards/{vCardId}'.format(v_card_id='v_card_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_virtual_cards(self):
        """Test case for list_virtual_cards

        Lista todos os cartões virtuais para um determinado cartão real
        """
        response = self.client.open(
            '/paySmart/ps-processadora/v1/cards/{cardId}/virtualcards/list'.format(card_id='card_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
