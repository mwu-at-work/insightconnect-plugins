import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
import time
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
            return {Output.SUCCESS: False, Output.EVENTINFO: {}}
        detail_search_status = self.connection.check_status_of_detail_search(id_)

        # check if status of
        # detail search is complete by checking if the completed property
        # in results is not equal to the contacted property

        for _ in range(0, 9999):
            if not detail_search_status:
                detail_search_status = self.connection.check_status_of_detail_search(id_)
                time.sleep(2)
            else:
                break

            response = self.connection.retrieve_results_for_detail_search(job_id=id_)
            data = insightconnect_plugin_runtime.helper.clean(response)

            return {
                Output.SUCCESS: True,
                Output.EVENTINFO: data,
            }
