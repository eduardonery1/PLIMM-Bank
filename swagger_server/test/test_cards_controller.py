# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.associate_anonymous_card_request import AssociateAnonymousCardRequest  # noqa: E501
from swagger_server.models.bind_card_result import BindCardResult  # noqa: E501
from swagger_server.models.card import Card  # noqa: E501
from swagger_server.models.card_block_and_reissue_request import CardBlockAndReissueRequest  # noqa: E501
from swagger_server.models.card_block_and_reissue_result import CardBlockAndReissueResult  # noqa: E501
from swagger_server.models.card_block_request import CardBlockRequest  # noqa: E501
from swagger_server.models.card_block_result import CardBlockResult  # noqa: E501
from swagger_server.models.card_list_result import CardListResult  # noqa: E501
from swagger_server.models.card_reissue_request import CardReissueRequest  # noqa: E501
from swagger_server.models.card_reissue_result import CardReissueResult  # noqa: E501
from swagger_server.models.card_single_list_result import CardSingleListResult  # noqa: E501
from swagger_server.models.card_unblock_request import CardUnblockRequest  # noqa: E501
from swagger_server.models.card_unblock_result import CardUnblockResult  # noqa: E501
from swagger_server.models.create_virtual_card_request import CreateVirtualCardRequest  # noqa: E501
from swagger_server.models.create_virtual_card_response import CreateVirtualCardResponse  # noqa: E501
from swagger_server.models.find_card_by_pan_request import FindCardByPANRequest  # noqa: E501
from swagger_server.models.list_virtual_cards_response import ListVirtualCardsResponse  # noqa: E501
from swagger_server.models.new_anonymous_card_request import NewAnonymousCardRequest  # noqa: E501
from swagger_server.models.new_anonymous_card_request_created_successfully import NewAnonymousCardRequestCreatedSuccessfully  # noqa: E501
from swagger_server.models.new_card_request import NewCardRequest  # noqa: E501
from swagger_server.models.new_cardrequest_created_successfully import NewCardrequestCreatedSuccessfully  # noqa: E501
from swagger_server.models.pin_change_created_successfully import PinChangeCreatedSuccessfully  # noqa: E501
from swagger_server.models.pin_change_request import PinChangeRequest  # noqa: E501
from swagger_server.models.result_data import ResultData  # noqa: E501
from swagger_server.models.update_card_request import UpdateCardRequest  # noqa: E501
from swagger_server.test import BaseTestCase


class TestCardsController(BaseTestCase):
    """CardsController integration test stubs"""

    def test_bind_card_to_cardholder(self):
        """Test case for bind_card_to_cardholder

        Associa um cartão não identificado a uma portador.
        """
        body = AssociateAnonymousCardRequest()
        headers = [('idempotency_key', '38400000-8cf0-11bd-b23e-10b96e4ef00d')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/cards/bindAnonymousCardRequest',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_block_and_reissue_card(self):
        """Test case for block_and_reissue_card

        Bloqueia o cartão {cardId} e emite um novo cartão para o cliente.
        """
        body = CardBlockAndReissueRequest()
        headers = [('idempotency_key', '38400000-8cf0-11bd-b23e-10b96e4ef00d')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/cards/{cardId}/blockAndReissueCardRequest'.format(card_id='card_id_example'),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_block_card(self):
        """Test case for block_card

        Bloqueia o cartão {cardId}. Não emite outro cartão.
        """
        body = CardBlockRequest()
        headers = [('idempotency_key', '38400000-8cf0-11bd-b23e-10b96e4ef00d')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/cards/{cardId}/blockCardRequest'.format(card_id='card_id_example'),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_change_pin(self):
        """Test case for change_pin

        Requisita uma mudança do PIN do cartão {cardId}.
        """
        body = PinChangeRequest()
        headers = [('idempotency_key', '38400000-8cf0-11bd-b23e-10b96e4ef00d')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/cards/{cardId}/changePin'.format(card_id='card_id_example'),
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

    def test_find_cards(self):
        """Test case for find_cards

        Recupera uma lista de cartões do emissor de acordo com os filtros definidos.
        """
        query_string = [('limit', 100),
                        ('starting_after', 'starting_after_example'),
                        ('ending_before', 'ending_before_example'),
                        ('issuer_id', 'issuer_id_example'),
                        ('identity_document_number', 'identity_document_number_example'),
                        ('pan_last_4_digits', 'pan_last_4_digits_example'),
                        ('issued_on_or_after_date', 'issued_on_or_after_date_example')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/cards',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_cards_by_pan(self):
        """Test case for find_cards_by_pan

        Recupera uma lista de cartões do emissor pelo PAN.
        """
        body = FindCardByPANRequest()
        response = self.client.open(
            '/paySmart/ps-processadora/v1/cards/findByPAN',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_card(self):
        """Test case for get_card

        Recupera informações de um cartão.
        """
        response = self.client.open(
            '/paySmart/ps-processadora/v1/cards/{cardId}'.format(card_id='card_id_example'),
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

    def test_reissue_card(self):
        """Test case for reissue_card

        Gera nova via do cartão para o cliente.
        """
        body = CardReissueRequest()
        headers = [('idempotency_key', '38400000-8cf0-11bd-b23e-10b96e4ef00d')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/cards/{cardId}/reissueCardRequest'.format(card_id='card_id_example'),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_request_new_anonymous_card(self):
        """Test case for request_new_anonymous_card

        Requisita um novo cartão \"não identificado\" que será associado a um usuário em um ponto futuro.
        """
        body = NewAnonymousCardRequest()
        headers = [('idempotency_key', '38400000-8cf0-11bd-b23e-10b96e4ef00d')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/cards/newAnonymousCardRequest',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_request_new_card(self):
        """Test case for request_new_card

        Requisita um novo cartão associado a conta.
        """
        body = NewCardRequest()
        headers = [('idempotency_key', '38400000-8cf0-11bd-b23e-10b96e4ef00d')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/accounts/{accountId}/newCardRequest'.format(account_id='account_id_example'),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_unblock_card(self):
        """Test case for unblock_card

        Desbloqueia o cartão {cardId}.
        """
        body = CardUnblockRequest()
        headers = [('idempotency_key', '38400000-8cf0-11bd-b23e-10b96e4ef00d')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/cards/{cardId}/unblockCardRequest'.format(card_id='card_id_example'),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_card(self):
        """Test case for update_card

        Atualiza informações do cartão, permitindo vincular um portador uma única vez.
        """
        body = UpdateCardRequest()
        response = self.client.open(
            '/paySmart/ps-processadora/v1/cards/{cardId}'.format(card_id='card_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
