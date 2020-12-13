# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.dispute import Dispute  # noqa: E501
from swagger_server.models.dispute_code import DisputeCode  # noqa: E501
from swagger_server.models.dispute_created_successfully import DisputeCreatedSuccessfully  # noqa: E501
from swagger_server.models.dispute_list_result import DisputeListResult  # noqa: E501
from swagger_server.models.dispute_request import DisputeRequest  # noqa: E501
from swagger_server.models.dispute_response_created_successfully import DisputeResponseCreatedSuccessfully  # noqa: E501
from swagger_server.models.dispute_response_request import DisputeResponseRequest  # noqa: E501
from swagger_server.models.dispute_reversal_created_successfully import DisputeReversalCreatedSuccessfully  # noqa: E501
from swagger_server.models.dispute_reversal_request import DisputeReversalRequest  # noqa: E501
from swagger_server.models.dispute_status import DisputeStatus  # noqa: E501
from swagger_server.models.result_data import ResultData  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDisputesController(BaseTestCase):
    """DisputesController integration test stubs"""

    def test_add_dispute(self):
        """Test case for add_dispute

        Registra uma disputa para questionar a validade de uma transação.
        """
        body = DisputeRequest()
        headers = [('idempotency_key', '38400000-8cf0-11bd-b23e-10b96e4ef00d')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/disputes',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_disputes(self):
        """Test case for find_disputes

        Recupera uma lista de disputas do emissor de acordo com os filtros definidos.
        """
        query_string = [('limit', 100),
                        ('starting_after', 'starting_after_example'),
                        ('ending_before', 'ending_before_example'),
                        ('dispute_reason', DisputeCode()),
                        ('dispute_status', DisputeStatus()),
                        ('beginning_date', 'beginning_date_example'),
                        ('ending_date', 'ending_date_example')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/disputes',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_dispute(self):
        """Test case for get_dispute

        Recupera informações de uma disputa.
        """
        response = self.client.open(
            '/paySmart/ps-processadora/v1/disputes/{disputeId}'.format(dispute_id='dispute_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_repond_dispute(self):
        """Test case for repond_dispute

        Responde a um parecer negativo da bandeira/credenciador. A resposta pode aceitar o parcer e desistir da disputa ou pode discordar e passar a disputa para a próxima fase.
        """
        body = DisputeResponseRequest()
        headers = [('idempotency_key', '38400000-8cf0-11bd-b23e-10b96e4ef00d')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/disputes/{disputeId}/response'.format(dispute_id='dispute_id_example'),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_undo_dispute(self):
        """Test case for undo_dispute

        Desiste de uma disputa e envia uma reversão dela.
        """
        body = DisputeReversalRequest()
        headers = [('idempotency_key', '38400000-8cf0-11bd-b23e-10b96e4ef00d')]
        response = self.client.open(
            '/paySmart/ps-processadora/v1/disputes/{disputeId}/undo'.format(dispute_id='dispute_id_example'),
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
