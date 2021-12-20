import insightconnect_plugin_runtime
from .schema import FindEventInput, FindEventOutput, Input, Output

# Custom imports below
from _datetime import datetime
from insightconnect_plugin_runtime.exceptions import PluginException


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
        device_external_ip = params.get(Input.DEVICE_EXTERNAL_IP)
        process_name = params.get(Input.PROCESS_NAME)
        enriched_event_type = params.get(Input.ENRICHED_EVENT_TYPE)
        process_hash = params.get(Input.PROCESS_HASH)
        device_name = params.get(Input.DEVICE_NAME)

        criteria = {}
        exclusions = {}

        if device_external_ip:
            criteria["device_external_ip"] = device_external_ip
        if process_name:
            criteria["process_name"] = [process_name]
        if enriched_event_type:
            criteria["enriched_event_type"] = enriched_event_type
        if process_hash:
            criteria["process_hash"] = [process_hash]
        if device_name:
            criteria["device_name"] = [device_name]
        if len(criteria) == 0:
            raise PluginException(
                cause="Error. Have not entered a criteria for action to run.",
                assistance="Enter a criteria of at least one plugin input.",
            )
        elif len(exclusions) > 0:
            if device_external_ip:
                exclusions["device_external_ip"] = device_external_ip
            if process_name:
                exclusions["process_name"] = [process_name]
            if enriched_event_type:
                exclusions["enriched_event_type"] = enriched_event_type
            if process_hash:
                exclusions["process_hash"] = [process_hash]
            if device_name:
                exclusions["device_name"] = [device_name]


        id_ = self.connection.get_job_id_for_enriched_event(criteria, exclusions=exclusions)

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
            Output.SUCCESS: True,
            Output.EVENTINFO: data,
        }
