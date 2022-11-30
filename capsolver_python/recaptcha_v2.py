from typing import Union
from .request_type import RequestType
from .proxy import *
from .useragent import *


class RecaptchaV2Task(UserAgent, Proxy):
    '''
    Class to solve Recaptcha v2 tasks with or without proxy.
    '''
    def __init__(self, client_key: str, beta: bool = False) -> None:
        super(RecaptchaV2Task, self).__init__(client_key, beta)

    def create_task(self, website_url: str,
                    website_key: str, cookies: Union[dict, list, str] = None, recaptcha_s_value: str = None, 
                    invisible: bool = False) -> str:
        '''
        Create Recaptcha V2 task
        '''
        data = {
            "clientKey": self.client_key,
            "task": {
                "type": "ReCaptchaV2Task",
                "websiteURL": website_url,
                "websiteKey": website_key,
                "isInvisible": invisible
            }
        }
        data, is_user_agent = self._add_user_agent(data)
        data, is_proxy = self._is_proxy_task(data)
        data = self._add_cookies(cookies, data)
        if recaptcha_s_value is not None:
            data["task"]["recaptchaDataSValue"] = recaptcha_s_value
        return self._make_request(RequestType.CreateTask, data).get("taskId")