from enum import Enum


class Result(Enum):
    SUCCESS = {"code": "000000", "message": "success"}
    FAIL = {"code": "999999", "message": "fail"}
    ERROR = {"code": "999998", "message": "error"}
    WARNING = {"code": "999997", "message": "warning"}
    INFO = {"code": "999996", "message": "info"}
    DEBUG = {"code": "999995", "message": "debug"}
    UNKNOWN = {"code": "999994", "message": "unknown"}
