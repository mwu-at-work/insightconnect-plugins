import insightconnect_plugin_runtime
from .schema import CheckForSquattersInput, CheckForSquattersOutput, Input, Output, Component

# Custom imports below
from komand_typo_squatter.util import utils


class CheckForSquatters(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="check_for_squatters",
            description=Component.DESCRIPTION,
            input=CheckForSquattersInput(),
            output=CheckForSquattersOutput(),
        )

    def run(self, params={}):
        return {
            Output.POTENTIAL_SQUATTERS: utils.check_for_squatters(
                params.get(Input.DOMAIN), params.get(Input.FLAG, ""), self.logger
            )
        }
