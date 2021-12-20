import sys
import os

sys.path.append(os.path.abspath("../tests/"))

from unittest import TestCase
from unittest.mock import patch


from komand_carbon_black_defense.actions.find_event import FindEvent
from komand_carbon_black_defense.actions.find_event.schema import Input as FindEventSchemaInput
from unit_tests.util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


class TestFindEvent(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request) -> None:
        cls.connection, cls.action = Util.default_connector(FindEvent())

    # approach: testing users input that could mess up action - user input changes / api changes
    # test not entering an org key
    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_job_id_for_enriched_event_empty_org_key(self, make_request):
        temp_org_key = self.action.connection.org_key
        self.action.connection.org_key = ""
        with self.assertRaises(PluginException) as exception:
            self.action.run({FindEventSchemaInput.PROCESS_NAME: "chrome.exe"})
        cause = "There's no org key input."
        self.assertEqual(exception.exception.cause, cause)
        self.action.connection.org_key = temp_org_key

    # test entering a valid org key
    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_job_id_for_enriched_event_valid_org_key(self, make_request):
        actual = self.action.connection.get_job_id_for_enriched_event({FindEventSchemaInput.PROCESS_NAME: "chrome.exe"})
        expected = Util.read_file_to_dict("payloads/post_with_valid_org_key_find_event.json.resp")["job_id"]
        self.assertEqual(expected, actual)

    # testing a user not entering a criteria to search by
    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_job_id_for_enriched_event_with_no_criteria(self, make_request):
        with self.assertRaises(PluginException) as exception:
            self.action.run({FindEventSchemaInput.PROCESS_NAME: ""})
        cause = "Error. Have not entered a criteria for action to run."
        self.assertEqual(exception.exception.cause, cause)

    # testing if the criteria type is correct
    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_job_id_for_enriched_event_with_criteria(self, make_request):
        actual = self.action.connection.get_job_id_for_enriched_event({FindEventSchemaInput.PROCESS_NAME: "chrome.exe"})
        expected = Util.read_file_to_dict("payloads/post_with_valid_org_key_find_event.json.resp")["job_id"]
        self.assertEqual(expected, actual)
