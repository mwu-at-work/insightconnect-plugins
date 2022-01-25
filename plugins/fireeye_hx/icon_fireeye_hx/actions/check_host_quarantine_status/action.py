import komand
from .schema import CheckHostQuarantineStatusInput, CheckHostQuarantineStatusOutput, Input, Output, Component

# Custom imports below


class CheckHostQuarantineStatus(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="check_host_quarantine_status",
            description=Component.DESCRIPTION,
            input=CheckHostQuarantineStatusInput(),
            output=CheckHostQuarantineStatusOutput(),
        )

    def run(self, params={}):
        agent_id = params.get(Input.AGENT_ID)
        return {
            Output.RESULTS: komand.helper.clean(self.connection.api.check_host_quarantine_status(agent_id).get("data"))
        }
