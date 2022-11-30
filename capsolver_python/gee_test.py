from typing import Union
from .request_type import RequestType
from .proxy import *
from .useragent import *


class GeeTestTask(UserAgent, Proxy):
    '''
    Class to solve GeeTest tasks with or without proxy.
    '''
    def __init__(self, client_key: str, beta: bool = False) -> None:
        super(GeeTestTask, self).__init__(client_key, beta)

    def create_task(self, website_url: str,
                    gt: str, challenge: str, get_lib: str,
                    api_server_subdomain: str = None,
                    version: int = None, init_parameters: str = None) -> str:
        '''
        Create GeeTest task
        '''
        data = {
            "clientKey": self.client_key,
            "task": {
                "type": "GeeTestTask",
                "websiteURL": website_url,
                "gt": gt,
                "challenge": challenge
            }
        }
        data, is_user_agent = self._add_user_agent(data)
        data, is_proxy = self._is_proxy_task(data)
        if api_server_subdomain is not None:
            data["task"]["geetestApiServerSubdomain"] = api_server_subdomain
        if version is not None:
            data["task"]["version"] = 3
        if get_lib is not None:
            data["task"]["geetestGetLib"] = get_lib
        if init_parameters is not None:
            data["task"]["initParameters"] = init_parameters
        return self._make_request(RequestType.CreateTask, data).get("taskId")