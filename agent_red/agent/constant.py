"""
Description
=====

All constant values in the agent are specified in here.
"""""

import os

PLAN_INIT = "INIT"
PLAN_WORKING = "WORKING"
PLAN_FAIL = "FAIL"
PLAN_SUCCEED = "SUCCEED"

STATE_VALUE_UNKNOWN = "UNKNOWN"

STATE_KEY_PROTOCOL = "protocol"
STATE_KEY_PRIVILEGE = "privilege"
STATE_KEY_ADDRESS = "address"
STATE_KEY_SHELL = "shell"

STATE_VALUE_PROTOCOL_IP = "ip"
STATE_VALUE_PRIVILEGE_ROOT = "0"
STATE_VALUE_SHELL_PERMANENT = "PERMANENT"

DEFAULT_LISTENER_PORT = "10000"
DEFAULT_LISTENER_IP = "127.0.0.1"
DEFAULT_TARGET_IP = "127.0.0.1"

CONDITION_OPERATOR_EQUAL = "EQ"
CONDITION_OPERATOR_NOT_EQUAL = "NEQ"
CONDITION_OPERATOR_EXIST = "EXIST"
CONDITION_OPERATOR_NOT_EXIST = "NOT EXIST"
CONDITION_OPERATOR_INCLUDE = "INCLUDE"

TEMPORARY_FILE_SHELL = os.sep + "tmp" + os.sep + "AAABBB"
