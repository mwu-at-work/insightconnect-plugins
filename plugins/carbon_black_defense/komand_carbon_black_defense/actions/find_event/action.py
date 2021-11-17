import insightconnect_plugin_runtime
from .schema import FindEventInput, FindEventOutput, Input, Output

# Custom imports below
from _datetime import datetime


class FindEvent(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="find_event",
            description="Retrieves all events matching the input search criteria. "
            "Response is a list of events in JSON format."
            "Resulting events are sorted in descending order of time",
            input=FindEventInput(),
            output=FindEventOutput(),
        )

    def run(self, params={}):
        process_name = params.get(Input.PROCESS_NAME)
        event_id = params.get(Input.EVENT_ID)
        id_ = self.connection.get_job_id_for_enriched_event(process_name=process_name, event_id=event_id)
        self.logger.info(f"Got enriched event job ID: {id_}")
        if id_ is None:
            return {Output.EVENTINFO: {}}
        enriched_event_search_status = self.connection.get_enriched_event_status(id_)

        t1 = datetime.now()
        for _ in range(0, 9999):
            if not enriched_event_search_status:
                enriched_event_search_status = self.connection.get_enriched_event_status(id_)
                if (datetime.now() - t1).seconds > 60:
                    break
            else:
                break
        response = self.connection.retrieve_results_for_enriched_event(job_id=id_)
        data = insightconnect_plugin_runtime.helper.clean(response)

        return {
            Output.EVENTINFO: data,
        }
