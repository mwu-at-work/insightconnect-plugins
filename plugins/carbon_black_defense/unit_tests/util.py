import logging
import sys
import os
import json

from komand_carbon_black_defense.connection.connection import Connection
from komand_carbon_black_defense.actions.find_event.schema import Input
from komand_carbon_black_defense.connection.schema import Input

from insightconnect_plugin_runtime.exceptions import PluginException


class Util:
    @staticmethod
    def read_file_to_dict(filename):
        with open(filename, "rt") as my_file:
            return json.loads(
                Util.read_file_to_string(os.path.join(os.path.dirname(os.path.realpath(__file__)), filename))
            )

    @staticmethod
    def read_file_to_string(filename):
        with open(filename, "rt") as my_file:
            return my_file.read()

    @staticmethod
    def mocked_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename):
                self.filename = filename

            def read(self):
                if self.filename == "error":
                    raise PluginException(preset=PluginException.Preset.SERVER_ERROR)
                if self.filename == "empty":
                    return {}
                file_path = os.path.join(
                    os.path.dirname(os.path.realpath(__file__)), "example_output", f"{self.filename}.json.resp"
                )
                file_text = Util.read_file_to_string(file_path)
                return file_text

    def mock_request(*args, **kwargs):
        class MockResponse:
            def __init__(self, status_code: int, filename: str = None):
                self.status_code = status_code
                if filename:
                    self.text = Util.read_file_to_string(
                        os.path.join(os.path.dirname(os.path.realpath(__file__)), f"{filename}.json.resp")
                    )
                else:
                    self.text = ""

            def json(self):
                return json.loads(self.text)

        # cases
        # the args are in relation to the call_api method in connection.py
        # testing user input for the org key and search criteria for the find event action helper method and get details action helper method

        if args[0] == "POST":  # get_job_id_for_enriched_event
            if "/search_jobs" in args[1]:
                if "org_key" not in args[1]:  # if org key is empty
                    return MockResponse(400, "payloads/post_no_org_key_find_event")
                if "invalid_org_key" in args[1]:
                    return MockResponse(403, "payloads/post_invalid_org_key_find_event")
                if "org_key" in args[1] and len(kwargs["json"]["criteria"]) > 0:
                    return MockResponse(200, "payloads/post_with_valid_org_key_find_event")
            elif "/detail_jobs" in args[1]:
                if "org_key" not in args[1]:  # if org key is empty
                    return MockResponse(400, "payloads/post_no_org_key_get_details")
                #  if "invalid_org_key":
                #     return MockResponse(403, "payloads/post_invalid_org_key_get_details")
                if "valid_org_key" in args[1] and len(kwargs["json"]["event_id"] > 0):
                    return MockResponse(200, "paylods/post_with_valid_org_key_get_details")

    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.CONNECTOR: "connector",
                Input.URL: "url",
                Input.API_KEY: {"secretKey": "api_key"},
                Input.ORG_KEY: "org_key",
            }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return default_connection, action
