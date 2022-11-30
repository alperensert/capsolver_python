from typing import Union
from .request_type import RequestType
from .proxy import *
from .useragent import *


class HCaptchaTask(UserAgent, Proxy):
    '''
    Class to solve HCaptcha tasks with or without proxy.
    '''
    def __init__(self, client_key: str, beta: bool = False) -> None:
        super(HCaptchaTask, self).__init__(client_key, beta)

    def create_task(self, website_url: str,
                    website_key: str, invisible: bool = None,
                    is_enterprise: bool = None, enterprise_payload: dict = None) -> str:
        '''
        Create HCaptcha task
        '''
        data = {
            "clientKey": self.client_key,
            "task": {
                "type": "HCaptchaTask",
                "websiteURL": website_url,
                "websiteKey": website_key
            }
        }
        data, is_user_agent = self._add_user_agent(data)
        data, is_proxy = self._is_proxy_task(data)
        if enterprise_payload is not None:
            data["task"]["enterprisePayload"] = enterprise_payload
        if invisible is not None:
            data["task"]["isInvisible"] = invisible
        if is_enterprise is not None:
            data["task"]["isEnterprise"] = is_enterprise
        return self._make_request(RequestType.CreateTask, data).get("taskId")