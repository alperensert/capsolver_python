from enum import Enum


class RequestType(str, Enum):
    GetBalance = "/getBalance"
    CreateTask = "/createTask"
    GetTaskResult = "/getTaskResult"
    CreateTaskKasada = "/kasada/invoke"
    CreateTaskAntiAkamai = "/akamaibmp/invoke"
