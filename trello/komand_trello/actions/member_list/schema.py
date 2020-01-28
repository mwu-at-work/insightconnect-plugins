# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "List members of organization"


class Input:
    ACTION_FIELDS = "action_fields"
    ACTIONS = "actions"
    ACTIONS_DISPLAY = "actions_display"
    ACTIONS_ENTITIES = "actions_entities"
    ACTIONS_LIMIT = "actions_limit"
    BOARD_ACTION_FIELDS = "board_action_fields"
    BOARD_ACTIONS = "board_actions"
    BOARD_ACTIONS_DISPLAY = "board_actions_display"
    BOARD_ACTIONS_ENTITIES = "board_actions_entities"
    BOARD_ACTIONS_FORMAT = "board_actions_format"
    BOARD_ACTIONS_LIMIT = "board_actions_limit"
    BOARD_ACTIONS_SINCE = "board_actions_since"
    BOARD_FIELDS = "board_fields"
    BOARD_LISTS = "board_lists"
    BOARD_PLUGINDATA = "board_pluginData"
    BOARDS = "boards"
    FIELDS = "fields"
    ID_OR_NAME = "id_or_name"
    MEMBER_ACTIVITY = "member_activity"
    MEMBER_FIELDS = "member_fields"
    MEMBERS = "members"
    MEMBERSINVITED = "membersInvited"
    MEMBERSINVITED_FIELDS = "membersInvited_fields"
    MEMBERSHIPS = "memberships"
    MEMBERSHIPS_MEMBER = "memberships_member"
    MEMBERSHIPS_MEMBER_FIELDS = "memberships_member_fields"
    PAID_ACCOUNT = "paid_account"
    PLUGINDATA = "pluginData"
    

class Output:
    ACTIVEBILLABLEMEMBERCOUNT = "activeBillableMemberCount"
    BILLABLEMEMBERCOUNT = "billableMemberCount"
    BOARDS = "boards"
    DESC = "desc"
    DESCDATA = "descData"
    DISPLAYNAME = "displayName"
    ID = "id"
    IDBOARDS = "idBoards"
    INVITATIONS = "invitations"
    INVITED = "invited"
    MEMBERS = "members"
    MEMBERSINVITED = "membersInvited"
    MEMBERSHIPS = "memberships"
    NAME = "name"
    PLUGINDATA = "pluginData"
    POWERUPS = "powerUps"
    PREFS = "prefs"
    PREMIUMFEATURES = "premiumFeatures"
    PRODUCTS = "products"
    URL = "url"
    

class MemberListInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "action_fields": {
      "type": "string",
      "title": "Action Fields",
      "description": "List all fields of actions",
      "default": "all",
      "enum": [
        "all",
        "data",
        "date",
        "idMemberCreator",
        "type"
      ],
      "order": 6
    },
    "actions": {
      "type": "string",
      "title": "List Actions",
      "description": "List actions",
      "enum": [
        "",
        "addAttachmentToCard",
        "addChecklistToCard",
        "addMemberToBoard",
        "addMemberToCard",
        "addMemberToOrganization",
        "addToOrganizationBoard",
        "commentCard",
        "convertToCardFromCheckItem",
        "copyBoard",
        "copyCard",
        "copyCommentCard",
        "createBoard",
        "createCard",
        "createList",
        "createOrganization",
        "deleteAttachmentFromCard",
        "deleteBoardInvitation",
        "deleteCard",
        "deleteOrganizationInvitation",
        "disablePowerUp",
        "emailCard",
        "enablePowerUp",
        "makeAdminOfBoard",
        "makeNormalMemberOfBoard",
        "makeNormalMemberOfOrganization",
        "makeObserverOfBoard",
        "memberJoinedTrello",
        "moveCardFromBoard",
        "moveCardToBoard",
        "moveListFromBoard",
        "moveListToBoard",
        "removeChecklistFromCard",
        "removeFromOrganizationBoard",
        "removeMemberFromCard",
        "unconfirmedBoardInvitation",
        "unconfirmedOrganizationInvitation",
        "updateBoard",
        "updateCard",
        "updateCard:closed",
        "updateCard:desc",
        "updateCard:idList",
        "updateCard:name",
        "updateCheckItemStateOnCard",
        "updateChecklist",
        "updateList",
        "updateList:closed",
        "updateList:name",
        "updateMember",
        "updateOrganization"
      ],
      "order": 2
    },
    "actions_display": {
      "type": "boolean",
      "title": "Actions Display",
      "description": "Actions display",
      "default": false,
      "order": 4
    },
    "actions_entities": {
      "type": "boolean",
      "title": "Actions Entities",
      "description": "Actions entities",
      "default": false,
      "order": 3
    },
    "actions_limit": {
      "type": "integer",
      "title": "Actions Limit",
      "description": "A number from 0 to 1000, default: 50",
      "default": 50,
      "order": 5
    },
    "board_action_fields": {
      "type": "string",
      "title": "Board Action Fields",
      "description": "Fields of board actions",
      "default": "all",
      "enum": [
        "all",
        "data",
        "date",
        "idMemberCreator",
        "type"
      ],
      "order": 24
    },
    "board_actions": {
      "type": "string",
      "title": "Board Actions",
      "description": "Board actions",
      "enum": [
        "",
        "all",
        "addAttachmentToCard",
        "addChecklistToCard",
        "addMemberToBoard",
        "addMemberToCard",
        "addMemberToOrganization",
        "addToOrganizationBoard",
        "commentCard",
        "convertToCardFromCheckItem",
        "copyBoard",
        "copyCard",
        "copyCommentCard",
        "createBoard",
        "createCard",
        "createList",
        "createOrganization",
        "deleteAttachmentFromCard",
        "deleteBoardInvitation",
        "deleteCard",
        "deleteOrganizationInvitation",
        "disablePowerUp",
        "emailCard",
        "enablePowerUp",
        "makeAdminOfBoard",
        "makeNormalMemberOfBoard",
        "makeNormalMemberOfOrganization",
        "makeObserverOfBoard",
        "memberJoinedTrello",
        "moveCardFromBoard",
        "moveCardToBoard",
        "moveListFromBoard",
        "moveListToBoard",
        "removeChecklistFromCard",
        "removeFromOrganizationBoard",
        "removeMemberFromCard",
        "unconfirmedBoardInvitation",
        "unconfirmedOrganizationInvitation",
        "updateBoard",
        "updateCard",
        "updateCard:closed",
        "updateCard:desc",
        "updateCard:idList",
        "updateCard:name",
        "updateCheckItemStateOnCard",
        "updateChecklist",
        "updateList",
        "updateList:closed",
        "updateList:name",
        "updateMember",
        "updateOrganization"
      ],
      "order": 18
    },
    "board_actions_display": {
      "type": "boolean",
      "title": "Board Actions Display",
      "description": "Board actions display",
      "default": false,
      "order": 20
    },
    "board_actions_entities": {
      "type": "boolean",
      "title": "Board Actions Entities",
      "description": "Board actions entities",
      "default": false,
      "order": 19
    },
    "board_actions_format": {
      "type": "string",
      "title": "Board Actions Format",
      "description": "Format of board actions",
      "default": "list",
      "enum": [
        "count",
        "list",
        "minimal"
      ],
      "order": 21
    },
    "board_actions_limit": {
      "type": "integer",
      "title": "Board Actions Limit",
      "description": "A number from 0 to 1000, default: 50",
      "default": 50,
      "order": 23
    },
    "board_actions_since": {
      "type": "string",
      "title": "Board Actions Since",
      "description": "Filter by a date, null or lastView",
      "order": 22
    },
    "board_fields": {
      "type": "string",
      "title": "Board Fields",
      "description": "Response with one or more fields of boards, default: all",
      "default": "all",
      "enum": [
        "all",
        "closed",
        "dateLastActivity",
        "dateLastView",
        "desc",
        "descData",
        "idOrganization",
        "invitations",
        "invited",
        "labelNames",
        "memberships",
        "name",
        "pinned",
        "powerUps",
        "prefs",
        "shortLink",
        "shortUrl",
        "starred",
        "subscribed",
        "url"
      ],
      "order": 17
    },
    "board_lists": {
      "type": "string",
      "title": "Board Lists",
      "description": "List board with status of: all, closed, open, none, default: none",
      "default": "none",
      "enum": [
        "all",
        "closed",
        "none",
        "open"
      ],
      "order": 25
    },
    "board_pluginData": {
      "type": "boolean",
      "title": "Board Plugin Data",
      "description": "Board plugin data",
      "default": false,
      "order": 26
    },
    "boards": {
      "type": "string",
      "title": "Boards",
      "description": "Filter boards with any status of board",
      "enum": [
        "",
        "all",
        "closed",
        "members",
        "open",
        "organization",
        "pinned",
        "public",
        "starred",
        "unpinned"
      ],
      "order": 16
    },
    "fields": {
      "type": "string",
      "title": "Fields Organization",
      "description": "Field of organization, default: name,displayName,desc,descData,URL,website,logoHash,products,powerUps",
      "enum": [
        "",
        "all",
        "billableMemberCount",
        "desc",
        "descData",
        "displayName",
        "idBoards",
        "invitations",
        "invited",
        "logoHash",
        "memberships",
        "name",
        "powerUps",
        "prefs",
        "premiumFeatures",
        "products",
        "url",
        "website"
      ],
      "order": 28
    },
    "id_or_name": {
      "type": "string",
      "title": "ID or Name",
      "description": "ID or name of organization",
      "order": 1
    },
    "member_activity": {
      "type": "boolean",
      "title": "Member Activity",
      "description": "Response with activity of member or none, works for premium organizations only",
      "default": false,
      "order": 12
    },
    "member_fields": {
      "type": "string",
      "title": "Member Fields",
      "description": "Response with one or more member fields, default: avatarHash,fullName,initials,username,confirmed",
      "enum": [
        "",
        "all",
        "avatarHash",
        "bio",
        "bioData",
        "confirmed",
        "fullName",
        "idPremOrgsAdmin",
        "initials",
        "memberType",
        "products",
        "status",
        "url",
        "username"
      ],
      "order": 11
    },
    "members": {
      "type": "string",
      "title": "Members",
      "description": "Filter members with roles: admins, normal, owners, none, all",
      "default": "none",
      "enum": [
        "admins",
        "all",
        "none",
        "normal",
        "owners"
      ],
      "order": 10
    },
    "membersInvited": {
      "type": "string",
      "title": "Members Invited",
      "description": "Filter invited members by roles: admins, normal, owners, none, all, default: none",
      "default": "none",
      "enum": [
        "admins",
        "all",
        "none",
        "normal",
        "owners"
      ],
      "order": 13
    },
    "membersInvited_fields": {
      "type": "string",
      "title": "Members Invited Fields",
      "description": "Response with one or more fields of invited members, default: avatarHash,fullName,initials,username,confirmed",
      "enum": [
        "",
        "all",
        "avatarHash",
        "bio",
        "bioData",
        "confirmed",
        "fullName",
        "idPremOrgsAdmin",
        "initials",
        "memberType",
        "products",
        "status",
        "url",
        "username"
      ],
      "order": 14
    },
    "memberships": {
      "type": "string",
      "title": "Memberships",
      "description": "List status of memberships",
      "default": "none",
      "enum": [
        "none",
        "all",
        "active",
        "admin",
        "deactivated",
        "me",
        "normal"
      ],
      "order": 7
    },
    "memberships_member": {
      "type": "boolean",
      "title": "Memberships Member",
      "description": "Response with memberships or none",
      "default": false,
      "order": 8
    },
    "memberships_member_fields": {
      "type": "string",
      "title": "Memberships Member Fields",
      "description": "Response with one or more member fields, default: fullName,username",
      "enum": [
        "",
        "all",
        "avatarHash",
        "bio",
        "bioData",
        "confirmed",
        "fullName",
        "idPremOrgsAdmin",
        "initials",
        "memberType",
        "products",
        "status",
        "url",
        "username"
      ],
      "order": 9
    },
    "paid_account": {
      "type": "boolean",
      "title": "Paid Account",
      "description": "Paid account",
      "default": false,
      "order": 27
    },
    "pluginData": {
      "type": "boolean",
      "title": "Plugin Data",
      "description": "Plugin data",
      "default": false,
      "order": 15
    }
  },
  "required": [
    "id_or_name"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class MemberListOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "activeBillableMemberCount": {
      "type": "integer",
      "title": "Active Billable Member Count",
      "description": "Active billable member count",
      "order": 14
    },
    "billableMemberCount": {
      "type": "integer",
      "title": "Billable Member Count",
      "description": "Billable member count",
      "order": 13
    },
    "boards": {
      "type": "array",
      "title": "Boards",
      "description": "Boards",
      "items": {
        "type": "string"
      },
      "order": 20
    },
    "desc": {
      "type": "string",
      "title": "Description About Organization",
      "description": "The description about organization",
      "order": 4
    },
    "descData": {
      "type": "object",
      "title": "Desc Data",
      "description": "Desc data",
      "order": 5
    },
    "displayName": {
      "type": "string",
      "title": "Display Name Organization",
      "description": "Display name organization",
      "order": 3
    },
    "id": {
      "type": "string",
      "title": "ID Organization",
      "description": "ID organization",
      "order": 1
    },
    "idBoards": {
      "type": "array",
      "title": "ID Boards",
      "description": "ID boards",
      "items": {
        "type": "string"
      },
      "order": 6
    },
    "invitations": {
      "type": "array",
      "title": "Invitations",
      "description": "Invitations",
      "items": {
        "type": "string"
      },
      "order": 8
    },
    "invited": {
      "type": "boolean",
      "title": "Invited",
      "description": "Invited",
      "order": 7
    },
    "members": {
      "type": "array",
      "title": "Members",
      "description": "Members",
      "items": {
        "type": "string"
      },
      "order": 19
    },
    "membersInvited": {
      "type": "array",
      "title": "Members Invited",
      "description": "The members invited",
      "items": {
        "type": "string"
      },
      "order": 17
    },
    "memberships": {
      "type": "array",
      "title": "Memberships",
      "description": "Memberships",
      "items": {
        "type": "string"
      },
      "order": 9
    },
    "name": {
      "type": "string",
      "title": "Name Organization",
      "description": "Name organization",
      "order": 2
    },
    "pluginData": {
      "type": "array",
      "title": "Plugin Data",
      "description": "Plugin's data",
      "items": {
        "type": "string"
      },
      "order": 18
    },
    "powerUps": {
      "type": "array",
      "title": "Power Ups",
      "description": "Power ups",
      "items": {
        "type": "integer"
      },
      "order": 11
    },
    "prefs": {
      "type": "object",
      "title": "Prefs",
      "description": "Prefs",
      "order": 10
    },
    "premiumFeatures": {
      "type": "array",
      "title": "Premium Features",
      "description": "Premium features",
      "items": {
        "type": "string"
      },
      "order": 16
    },
    "products": {
      "type": "array",
      "title": "Products",
      "description": "Products",
      "items": {
        "type": "integer"
      },
      "order": 12
    },
    "url": {
      "type": "string",
      "title": "URL",
      "description": "URL",
      "order": 15
    }
  },
  "required": [
    "id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
