from unittest import TestCase
from komand_typo_squatter.actions.check_for_squatters import CheckForSquatters
from komand_typo_squatter.actions.check_for_squatters.schema import Input, Output
from parameterized import parameterized
from unit_test.util import Util
from unittest.mock import patch


@patch("subprocess.run", side_effect=Util.mocked_run)
class TestCheckForSquatters(TestCase):
    @parameterized.expand(Util.load_parameters("check_for_squatters_parameters").get("parameters"))
    def test_check_for_squatters(self, mock_run, name, domain, flag, expected):
        action = CheckForSquatters()
        actual = action.run({Input.DOMAIN: domain, Input.FLAG: flag})
        expected = {Output.POTENTIAL_SQUATTERS: expected}
        self.assertEqual(actual, expected)
