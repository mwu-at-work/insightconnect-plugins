import insightconnect_plugin_runtime
from .schema import GetDetailsForSpecificEventInput, GetDetailsForSpecificEventOutput, Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException

import time
from _datetime import datetime


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
        if len(event_id) == 0:
            raise PluginException(
                cause="Error. Have not entered an event ID for action to run.",
                assistance="Please enter an event ID for the action to run.",
            )
        if type(event_id) is not list:
            raise PluginException(
                cause="Error. Event ID must be an array of a string.",
                assistance="Please convert the data type of event ID into an array of a string.",
            )
        id_ = self.connection.get_job_id_for_detail_search(event_ids=event_id)
        self.logger.info(f"Got job ID for detail search: {id_}")
        if id_ is None:
            return {Output.SUCCESS: False, Output.EVENTINFO: {}}
        detail_search_status = self.connection.check_status_of_detail_search(id_)

        # check if status of
        # detail search is complete by checking if the completed property
        # in results is not equal to the contacted property
        t1 = datetime.now()
        for _ in range(0, 9999):
            if not detail_search_status:
                detail_search_status = self.connection.check_status_of_detail_search(id_)
                if (datetime.now() - t1).seconds > 60:
                    break
            else:
                time.sleep(3)
            response = self.connection.retrieve_results_for_detail_search(job_id=id_)
            data = insightconnect_plugin_runtime.helper.clean(response)

            return {
                Output.SUCCESS: True,
                Output.EVENTINFO: data,
            }
