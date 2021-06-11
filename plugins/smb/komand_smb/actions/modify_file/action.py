import komand
from .schema import ModifyFileInput, ModifyFileOutput, Input, Output, Component
from komand.exceptions import PluginException

# Custom imports below
import io
import smb


class ModifyFile(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='modify_file',
                description=Component.DESCRIPTION,
                input=ModifyFileInput(),
                output=ModifyFileOutput())

    def run(self, params={}):
        file_path = params.get(Input.FILE_PATH)
        share_name = params.get(Input.SHARE_NAME)
        timeout = params.get(Input.TIMEOUT, 30)

        try:
            # Uncomment below line to see the SMB version
            #print(f'connection is {self.connection.conn.is_using_smb2}')
            self.connection.conn.resetFileAttributes(share_name, file_path, timeout=timeout)
        except smb.smb_structs.OperationFailure as e:
            raise PluginException(cause='Failed to reset file attributes',
                                  assistance='This may occur when the file does not exist.',
                                  data=e)
        except smb.base.SMBTimeout as e:
            raise PluginException(cause='Timeout reached when connecting to SMB endpoint.',
                                  assistance='Validate network connectivity.',
                                  data=e)
        except smb.base.NotReadyError as e:
            raise PluginException(cause='The SMB connection is not authenticated or the authentication has failed.',
                                  assistance='Verify the credentials of the connection in use.',
                                  data=e)

        return {Output.SUCCESS: True}
