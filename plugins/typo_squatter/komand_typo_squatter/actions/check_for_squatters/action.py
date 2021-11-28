import insightconnect_plugin_runtime
from .schema import CheckForSquattersInput, CheckForSquattersOutput, Input, Output, Component

# Custom imports below
import json
from komand_typo_squatter.util import utils
import subprocess


class CheckForSquatters(insightconnect_plugin_runtime.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="check_for_squatters",
            description=Component.DESCRIPTION,
            input=CheckForSquattersInput(),
            output=CheckForSquattersOutput(),
        )

    def run(self, params={}):
        domain = params.get(Input.DOMAIN)
        flag = params.get(Input.FLAG)
        flag = "" if not flag else (flag if flag[0:2] == "--" or flag[0:1] == "-" else "--" + flag)
        cmd = f"dnstwist {flag} -f json {domain}" if flag else f"dnstwist -f json {domain}"
        self.logger.info(f"Running command: {cmd}")
        results = subprocess.run(cmd.split(" "), stdout=subprocess.PIPE)
        js = json.loads(results.stdout.decode().replace("\\n", ""))
        for _, item in enumerate(js):
            js[_]["phishing_score"] = utils.score_domain(js[_].get("domain-name"))
        return {Output.POTENTIAL_SQUATTERS: js}
