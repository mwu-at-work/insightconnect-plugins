from unittest import TestCase, mock
from komand.exceptions import PluginException
from komand_active_directory_ldap.actions.modify_object import ModifyObject
from komand_active_directory_ldap.actions.modify_object.schema import Input, Output
from unit_test.common import MockServer
from unit_test.common import MockConnection
from unit_test.common import default_connector


class TestActionModifyObject(TestCase):
    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=ModifyObject())
    def test_modify_object(self, action):
        actual = action.run({Input.DISTINGUISHED_NAME: "CN=Users,DC=example,DC=com"})
        expected = {Output.SUCCESS: True}

        self.assertEqual(actual, expected)

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=ModifyObject())
    def test_modify_object_false(self, action):
        actual = action.run({Input.DISTINGUISHED_NAME: "CN=wrong_result,DC=example,DC=com"})
        expected = {Output.SUCCESS: False}

        self.assertEqual(actual, expected)

    @mock.patch("ldap3.Server", mock.MagicMock(return_value=MockServer))
    @mock.patch("ldap3.Connection", mock.MagicMock(return_value=MockConnection()))
    @default_connector(action=ModifyObject())
    def test_modify_group_group_not_found(self, action):
        with self.assertRaises(PluginException) as context:
            action.run({Input.DISTINGUISHED_NAME: "CN=empty_search,DC=example,DC=com"})

        self.assertEqual("The DN was not found.", context.exception.cause)
        self.assertEqual("The DN CN=empty_search,DC=example,DC=com was not found", context.exception.assistance)
