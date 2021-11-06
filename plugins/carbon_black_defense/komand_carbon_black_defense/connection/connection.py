import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import ConnectionTestException

# Custom imports below
import requests
from typing import Optional
import json


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

        self.job_id = None

    def connect(self, params=None):
        if params is None:
            params = {}
        self.logger.info("Connect: Connecting..")
        self.host = params.get(Input.URL)
        self.token = params.get(Input.API_KEY).get("secretKey")
        self.org_key = params.get(Input.ORG_KEY)
        self.connector = params.get(Input.CONNECTOR)
        self.headers = {"X-Auth-Token": f"{self.token}/{self.connector}"}

    def get_job_id_for_detail_search(self, event_id: str) -> Optional[str]:
        response = self.call_api(
            "POST",
            f"{self.host}/api/investigate/v2/orgs/{self.org_key}/enriched_events/detail_jobs",
            json_data={"event_ids": [event_id]},
        ).get("job_id")
        self.logger.info(f"The response is: {response}")
        if response:
            job_id = response
            return job_id
        return None

    def check_status_of_detail_search(self, job_id: str = None):
        response = self.call_api(
            "GET",
            f"{self.host}/api/investigate/v2/orgs/{self.org_key}/enriched_events/detail_jobs/" f"{job_id}",
            json_data={"job_id": job_id},
        )
        self.logger.info(f"{response}")
        contacted = response.get("contacted")
        completed = response.get("completed")
        if contacted and completed and (contacted == completed):
            return True
        return False

    def retrieve_results_for_detail_search(self, job_id: str):
        results = self.call_api(
            "GET",
            f"{self.host}/api/investigate/v2/orgs/{self.org_key}/enriched_events/detail_jobs/" f"{job_id}/results",
            json_data={"job_id": job_id},
        )
        self.logger.info(f"Retrieve results are: {results}")
        return results

    def call_api(self, method: str, url: str, params: dict = None, data: str = None, json_data: object = None):
        try:
            response = requests.request(method, url, headers=self.headers, params=params, data=data, json=json_data)

            self.logger.info(f"The response is:{response.text}")
            if 200 <= response.status_code < 300:
                return response.json()
            if 400 <= response.status_code < 500:
                raise PluginException(
                    preset=PluginException.Preset.UNKNOWN,
                    data=response.text,
                )
            if response.status_code >= 500:
                raise PluginException(preset=PluginException.Preset.SERVER_ERROR, data=response.text)

        except json.decoder.JSONDecodeError as e:
            raise PluginException(
                cause="Received an unexpected response from the server.",
                assistance="(non-JSON or no response was received).",
                data=e,
            )


"""""
    def test(self):
        host = self.host
        token = self.token
        connector = self.connector
        devices = f"/appservices/v6/orgs/{self.org_key}/devices/_search"
        headers = {"X-Auth-Token": f"{token}/{connector}"}
        url = host + devices

        result = requests.get(url, headers=headers)
        if result.status_code == 200:
            return {"success": True}
        if result.status_code == 401:
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
        raise ConnectionTestException(
            f"An unknown error occurred. Response code was: {result.status_code}"
            f" If the problem persists please contact support for help. Response was: {result.text}"
        )
""" ""
