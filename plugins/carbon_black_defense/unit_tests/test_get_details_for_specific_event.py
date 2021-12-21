import sys
import os

sys.path.append(os.path.abspath("../tests/"))

from unittest import TestCase
from unittest.mock import patch

from komand_carbon_black_defense.actions.get_details_for_specific_event import GetDetailsForSpecificEvent
from komand_carbon_black_defense.actions.get_details_for_specific_event.schema import \
    Input as GetDetailsForSpecificEventtSchemaInput
from unit_tests.util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


class TestGetDetailsForSpecificEvent(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request) -> None:
        cls.connection, cls.action = Util.default_connector(GetDetailsForSpecificEvent())

    # approach: testing users input that could mess up action - user input changes / api changes
    # test not entering an org key
    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_job_id_for_detail_search_empty_org_key(self, make_request):
        temp_org_key = self.action.connection.org_key
        self.action.connection.org_key = ""
        with self.assertRaises(PluginException) as exception:
            self.action.connection.get_job_id_for_detail_search({GetDetailsForSpecificEventtSchemaInput.EVENT_ID: "1234"})
        cause = "There's no org key input."
        self.assertEqual(exception.exception.cause, cause)
        self.action.connection.org_key = temp_org_key

    # testing a user not entering any event id to search by
    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_job_id_for_detail_search_with_no_event_id(self, make_request):
        with self.assertRaises(PluginException) as exception:
            self.action.run({GetDetailsForSpecificEventtSchemaInput.EVENT_ID: []})
        cause = "Error. Have not entered an event ID for action to run."
        self.assertEqual(exception.exception.cause, cause)

    # testing if a plugin exception is raised due to an incorrect event ID type
    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_job_id_for_detail_search_with_incorrect_event_id_type(self, make_request):
        with self.assertRaises(PluginException) as exception:
            self.action.run(
                {GetDetailsForSpecificEventtSchemaInput.EVENT_ID: {"1234"}})
        cause = "Error. Event ID must be an array of a string."
        self.assertEqual(exception.exception.cause, cause)
