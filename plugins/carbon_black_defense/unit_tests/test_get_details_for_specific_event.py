from unittest import TestCase
import json
import logging
from komand_carbon_black_defense.connection.connection import Connection
from komand_carbon_black_defense.actions.get_details_for_specific_event import GetDetailsForSpecificEvent
from insightconnect_plugin_runtime.exceptions import PluginException
import sys
import os

sys.path.append(os.path.abspath("../tests/"))


class TestGetDetailsForSpecificEvent(TestCase):
    def test_integration_get_details_for_specific_event(self):

        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = GetDetailsForSpecificEvent()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("../tests/get_details_for_specific_event.json", encoding="utf-8") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except PluginException:
            message = """
            Could not find or read sample tests from /tests directory

            An exception here likely means you didn't fill out your samples correctly in the /tests directory
            Please use 'icon-plugin generate samples', and fill out the resulting test files in the /tests directory
        """
            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)

        self.assertIsNotNone(results)
