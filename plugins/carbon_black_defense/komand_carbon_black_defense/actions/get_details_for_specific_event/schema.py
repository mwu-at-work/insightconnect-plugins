# GENERATED BY KOMAND SDK - DO NOT EDIT
import insightconnect_plugin_runtime
import json


class Component:
    DESCRIPTION = "Retrieve details for an individual event given the event ID"


class Input:
    EVENT_ID = "event_id"
    

class Output:
    EVENTINFO = "eventinfo"
    

class GetDetailsForSpecificEventInput(insightconnect_plugin_runtime.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "event_id": {
      "type": "string",
      "title": "Event ID",
      "description": "Event ID",
      "order": 1
    }
  },
  "required": [
    "event_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetDetailsForSpecificEventOutput(insightconnect_plugin_runtime.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "eventinfo": {
      "$ref": "#/definitions/event_info",
      "title": "Event Info",
      "description": "Detailed information on the event",
      "order": 1
    }
  },
  "definitions": {
    "event_info": {
      "type": "object",
      "title": "event_info",
      "properties": {
        "backend_timestamp": {
          "type": "string",
          "title": "Backend Timestamp",
          "description": "Backend timestamp",
          "order": 56
        },
        "device_external_ip": {
          "type": "string",
          "title": "Device External Ip",
          "description": "Device external ip",
          "order": 38
        },
        "device_group_id": {
          "type": "integer",
          "title": "Device Group Id",
          "description": "Device group id",
          "order": 8
        },
        "device_id": {
          "type": "integer",
          "title": "Device Id",
          "description": "Device id",
          "order": 48
        },
        "device_installed_by": {
          "type": "string",
          "title": "Device Installed By",
          "description": "Device installed by",
          "order": 21
        },
        "device_internal_ip": {
          "type": "string",
          "title": "Device Internal Ip",
          "description": "Device internal ip",
          "order": 42
        },
        "device_location": {
          "type": "string",
          "title": "Device Location",
          "description": "Device location",
          "order": 51
        },
        "device_name": {
          "type": "string",
          "title": "Device Name",
          "description": "Device name",
          "order": 55
        },
        "device_os": {
          "type": "string",
          "title": "Device Os",
          "description": "Device os",
          "order": 46
        },
        "device_os_version": {
          "type": "string",
          "title": "Device Os Version",
          "description": "Device os version",
          "order": 53
        },
        "device_policy": {
          "type": "string",
          "title": "Device Policy",
          "description": "Device policy",
          "order": 58
        },
        "device_policy_id": {
          "type": "integer",
          "title": "Device Policy Id",
          "description": "Device policy id",
          "order": 47
        },
        "device_target_priority": {
          "type": "string",
          "title": "Device Target Priority",
          "description": "Device target priority",
          "order": 3
        },
        "device_timestamp": {
          "type": "string",
          "title": "Device Timestamp",
          "description": "Device timestamp",
          "order": 15
        },
        "document_guid": {
          "type": "string",
          "title": "Document Guid",
          "description": "Document guid",
          "order": 24
        },
        "enriched": {
          "type": "boolean",
          "title": "Enriched",
          "description": "Enriched",
          "order": 27
        },
        "enriched_event_type": {
          "type": "string",
          "title": "Enriched Event Type",
          "description": "Enriched event type",
          "order": 26
        },
        "event_description": {
          "type": "string",
          "title": "Event Description",
          "description": "Event description",
          "order": 19
        },
        "event_id": {
          "type": "string",
          "title": "Event Id",
          "description": "Event id",
          "order": 22
        },
        "event_network_inbound": {
          "type": "boolean",
          "title": "Event Network Inbound",
          "description": "Event network inbound",
          "order": 49
        },
        "event_network_local_ipv4": {
          "type": "string",
          "title": "Event Network Local Ipv4",
          "description": "Event network local ipv4",
          "order": 43
        },
        "event_network_location": {
          "type": "string",
          "title": "Event Network Location",
          "description": "Event network location",
          "order": 1
        },
        "event_network_protocol": {
          "type": "string",
          "title": "Event Network Protocol",
          "description": "Event network protocol",
          "order": 30
        },
        "event_network_remote_ipv4": {
          "type": "string",
          "title": "Event Network Remote Ipv4",
          "description": "Event network remote ipv4",
          "order": 33
        },
        "event_network_remote_port": {
          "type": "integer",
          "title": "Event Network Remote Port",
          "description": "Event network remote port",
          "order": 7
        },
        "event_report_code": {
          "type": "string",
          "title": "Event Report Code",
          "description": "Event report code",
          "order": 40
        },
        "event_threat_score": {
          "type": "array",
          "title": "Event Threat Score",
          "description": "Event threat score",
          "items": {
            "type": "integer"
          },
          "order": 41
        },
        "event_type": {
          "type": "string",
          "title": "Event Type",
          "description": "Event type",
          "order": 4
        },
        "ingress_time": {
          "type": "integer",
          "title": "Ingress Time",
          "description": "Ingress time",
          "order": 45
        },
        "legacy": {
          "type": "boolean",
          "title": "Legacy",
          "description": "Legacy",
          "order": 10
        },
        "netconn_domain": {
          "type": "string",
          "title": "Netconn Domain",
          "description": "Netconn domain",
          "order": 18
        },
        "netconn_inbound": {
          "type": "boolean",
          "title": "Netconn Inbound",
          "description": "Netconn inbound",
          "order": 5
        },
        "netconn_ipv4": {
          "type": "integer",
          "title": "Netconn Ipv4",
          "description": "Netconn ipv4",
          "order": 39
        },
        "netconn_local_ipv4": {
          "type": "integer",
          "title": "Netconn Local Ipv4",
          "description": "Netconn local ipv4",
          "order": 28
        },
        "netconn_local_port": {
          "type": "integer",
          "title": "Netconn Local Port",
          "description": "Netconn local port",
          "order": 52
        },
        "netconn_location": {
          "type": "string",
          "title": "Netconn Location",
          "description": "Netconn location",
          "order": 16
        },
        "netconn_port": {
          "type": "integer",
          "title": "Netconn Port",
          "description": "Netconn port",
          "order": 13
        },
        "netconn_protocol": {
          "type": "string",
          "title": "Netconn Protocol",
          "description": "Netconn protocol",
          "order": 14
        },
        "org_id": {
          "type": "string",
          "title": "Org Id",
          "description": "Org id",
          "order": 54
        },
        "parent_effective_reputation": {
          "type": "string",
          "title": "Parent Effective Reputation",
          "description": "Parent effective reputation",
          "order": 35
        },
        "parent_effective_reputation_source": {
          "type": "string",
          "title": "Parent Effective Reputation Source",
          "description": "Parent effective reputation source",
          "order": 31
        },
        "parent_guid": {
          "type": "string",
          "title": "Parent Guid",
          "description": "Parent guid",
          "order": 23
        },
        "parent_hash": {
          "type": "array",
          "title": "Parent Hash",
          "description": "Parent hash",
          "items": {
            "type": "string"
          },
          "order": 29
        },
        "parent_name": {
          "type": "string",
          "title": "Parent Name",
          "description": "Parent name",
          "order": 37
        },
        "parent_pid": {
          "type": "integer",
          "title": "Parent Pid",
          "description": "Parent pid",
          "order": 57
        },
        "parent_reputation": {
          "type": "string",
          "title": "Parent Reputation",
          "description": "Parent reputation",
          "order": 59
        },
        "process_cmdline": {
          "type": "array",
          "title": "Process Cmdline",
          "description": "Process cmdline",
          "items": {
            "type": "string"
          },
          "order": 20
        },
        "process_cmdline_length": {
          "type": "array",
          "title": "Process Cmdline Length",
          "description": "Process cmdline length",
          "items": {
            "type": "integer"
          },
          "order": 25
        },
        "process_effective_reputation": {
          "type": "string",
          "title": "Process Effective Reputation",
          "description": "Process effective reputation",
          "order": 6
        },
        "process_effective_reputation_source": {
          "type": "string",
          "title": "Process Effective Reputation Source",
          "description": "Process effective reputation source",
          "order": 9
        },
        "process_guid": {
          "type": "string",
          "title": "Process Guid",
          "description": "Process guid",
          "order": 50
        },
        "process_hash": {
          "type": "array",
          "title": "Process Hash",
          "description": "Process hash",
          "items": {
            "type": "string"
          },
          "order": 34
        },
        "process_name": {
          "type": "string",
          "title": "Process Name",
          "description": "Process name",
          "order": 2
        },
        "process_pid": {
          "type": "array",
          "title": "Process Pid",
          "description": "Process pid",
          "items": {
            "type": "integer"
          },
          "order": 32
        },
        "process_reputation": {
          "type": "string",
          "title": "Process Reputation",
          "description": "Process reputation",
          "order": 44
        },
        "process_sha256": {
          "type": "string",
          "title": "Process Sha256",
          "description": "Process sha256",
          "order": 36
        },
        "process_start_time": {
          "type": "string",
          "title": "Process Start Time",
          "description": "Process start time",
          "order": 11
        },
        "process_username": {
          "type": "array",
          "title": "Process Username",
          "description": "Process username",
          "items": {
            "type": "string"
          },
          "order": 12
        },
        "ttp": {
          "type": "array",
          "title": "Ttp",
          "description": "Ttp",
          "items": {
            "type": "string"
          },
          "order": 17
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
