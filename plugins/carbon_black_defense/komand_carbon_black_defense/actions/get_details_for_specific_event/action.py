import insightconnect_plugin_runtime
from .schema import GetDetailsForSpecificEventInput, GetDetailsForSpecificEventOutput, Input, Output


class GetDetailsForSpecificEvent(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_details_for_specific_event",
            description="Retrieve details for an individual event given the event ID",
            input=GetDetailsForSpecificEventInput(),
            output=GetDetailsForSpecificEventOutput(),
        )

    def run(self, params={}):

        event_id = params.get(Input.EVENT_ID)
        id_ = self.connection.get_job_id_for_detail_search(event_id=event_id)

        if id_ is None:
            return {Output.EVENTINFO: {}}
        detail_search_status = self.connection.check_status_of_detail_search(id_)

        # check if status of
        # detail search is complete by checking if the completed property
        # in results is not equal to the contacted property

        if not detail_search_status:
            self.connection.check_status_of_detail_search(id_)
        else:
            self.connection.retrieve_results_for_detail_search()

        try:
            response = self.connection.retrieve_results_for_detail_search()
            data = insightconnect_plugin_runtime.helper.clean(response.json())

            if response.status_code == 200 and "eventInfo" in data:

                return {
                    Output.EVENTINFO: data["eventInfo"],
                }

        except ValueError:
            self.logger.error(response.text)
            raise Exception(
                f"Error: Received an unexpected response"
                f" (non-JSON or no response was received). Raw response in logs."
            )

        if response.status_code in range(400, 499):
            raise Exception(
                f"Carbon Black returned a {response.status_code} code."
                f" Verify the token and host configuration in the connection. Response was: {response.text}"
            )
        if response.status_code in range(500, 599):
            raise Exception(
                f"Carbon Black returned a {response.status_code} code."
                f" If the problem persists please contact support for help. Response was: {response.text}"
            )
        self.logger.error(response.text)
        raise Exception(
            f"An unknown error occurred."
            f" Carbon Black returned a {response.status_code} code. Contact support for help. Raw response in logs."
        )
