# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Delete organization membership"


class Input:
    MEMBERSHIP_ID = "membership_id"
    

class Output:
    STATUS = "status"
    

class DeleteMembershipInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "membership_id": {
      "type": "integer",
      "title": "Membership ID",
      "description": "ID of membership to delete E.g. 1401295821555",
      "order": 1
    }
  },
  "required": [
    "membership_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class DeleteMembershipOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "status": {
      "type": "boolean",
      "title": "Status",
      "description": "Success or failure",
      "order": 1
    }
  },
  "required": [
    "status"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
