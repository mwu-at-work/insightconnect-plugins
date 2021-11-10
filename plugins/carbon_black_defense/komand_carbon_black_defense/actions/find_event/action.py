import insightconnect_plugin_runtime
from .schema import FindEventInput, FindEventOutput, Input, Output

# Custom imports below
import time


class FindEvent(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="find_event",
            description="Retrieves all events matching the input search criteria. Response is a list of events in JSON format. Resulting events are sorted in descending order of time",
            input=FindEventInput(),
            output=FindEventOutput(),
        )

    def run(self, params=None):
        if params is None:
            params = {}
        process_name = params.get(Input.PROCESS_NAME)
        event_id = params.get(Input.EVENT_ID)
        id_ = self.connection.get_job_id_for_enriched_event(process_name=process_name, event_id=event_id)
        self.logger.info(f"The id is: {id_}")
        if id_ is None:
            return {Output.EVENTINFO: {}}
        enriched_event_search_status = self.connection.get_enriched_event_status(id_)

        for _ in range(0, 9999):
            if not enriched_event_search_status:
                enriched_event_search_status = self.connection.get_enriched_event_status(id_)
                time.sleep(2)
            else:
                break
        response = self.connection.retrieve_results_for_enriched_event(job_id=id_)
        data = insightconnect_plugin_runtime.helper.clean(response)
        self.logger.info(f"The data is: {data}")

        return {
            Output.EVENTINFO: data,
        }
