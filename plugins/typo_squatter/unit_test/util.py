import json
import os


class Util:
    @staticmethod
    def read_file_to_string(filename):
        with open(filename) as my_file:
            return my_file.read()

    @staticmethod
    def load_parameters(filename):
        return json.loads(
            Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{filename}.json.resp")
            )
        )

    @staticmethod
    def mocked_run(*args, **kwargs):
        class MockRun:
            def __init__(self, filename):
                self.stdout = self.load_data(filename)

            def load_data(self, filename):
                return Util.read_file_to_string(
                    os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{filename}.json.resp")
                ).encode()

        if args[0] == ["dnstwist", "-r", "-s", "-m", "-f", "json", "rapid7.com"]:
            return MockRun("check_for_squatters_ssdeep_and_mxcheck")
        if args[0] == ["dnstwist", "--registered", "--whois", "-f", "json", "rapid7.com"]:
            return MockRun("check_for_squatters_whois_flag")
        if args[0] == ["dnstwist", "-r", "-g", "-f", "json", "rapid7.com"]:
            return MockRun("check_for_squatters_geoip_flag")
        if args[0] == ["dnstwist", "--registered", "-f", "json", "rapid7.com"]:
            return MockRun("check_for_squatters_with_flag")
        if args[0] == ["dnstwist", "-f", "json", "rapid7.com"]:
            return MockRun("check_for_squatters_without_flag")
        raise Exception("Not implemented")
