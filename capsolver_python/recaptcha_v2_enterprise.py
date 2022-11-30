from typing import Union
from .request_type import RequestType
from .proxy import *
from .useragent import *


class RecaptchaV2EnterpriseTask(UserAgent, Proxy):
    '''
    Class to solve Recaptcha v2 enterprise tasks with or without proxy.
    '''
    def __init__(self, client_key: str, beta: bool = False) -> None:
        super(RecaptchaV2EnterpriseTask, self).__init__(client_key, beta)

    def create_task(self, website_url: str,
                    website_key: str, cookies: Union[dict, list, str] = None, api_domain: str = None, 
                    enterprise_payload: dict = None) -> str:
        '''
        Create Recaptcha V2 Enterprise task
        '''
        data = {
            "clientKey": self.client_key,
            "task": {
                "type": "ReCaptchaV2EnterpriseTask",
                "websiteURL": website_url,
                "websiteKey": website_key
            }
        }
        data, is_user_agent = self._add_user_agent(data)
        data, is_proxy = self._is_proxy_task(data)
        data = self._add_cookies(cookies, data)
        if api_domain is not None:
            data["task"]["apiDomain"] = api_domain
        if enterprise_payload is not None:
            data["task"]["enterprisePayload"] = enterprise_payload
        return self._make_request(RequestType.CreateTask, data).get("taskId")