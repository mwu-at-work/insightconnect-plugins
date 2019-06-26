# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "List tags for this project"


class Input:
    PROJECT_NAME = "project_name"
    

class Output:
    TAGS = "tags"
    

class ListTagsInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "project_name": {
      "type": "string",
      "title": "Project Name",
      "order": 1
    }
  },
  "required": [
    "project_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class ListTagsOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "tags": {
      "type": "array",
      "title": "Tags",
      "items": {
        "$ref": "#/definitions/Tag"
      },
      "order": 1
    }
  },
  "required": [
    "tags"
  ],
  "definitions": {
    "Tag": {
      "type": "object",
      "title": "Tag",
      "properties": {
        "id": {
          "type": "integer",
          "title": "ID",
          "description": "Tag ID",
          "order": 1
        },
        "tag": {
          "type": "string",
          "title": "Name",
          "description": "Tag name",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
