from typing import Union
from .request_type import RequestType
from .proxy import *
from .useragent import *


class RecaptchaV3Task(UserAgent, Proxy):
    '''
    Class to solve Recaptcha v3 tasks with or without proxy.
    '''
    def __init__(self, client_key: str, beta: bool = False) -> None:
        super(RecaptchaV3Task, self).__init__(client_key, beta)

    def create_task(self, website_url: str,
                    website_key: str, page_action: str = "verify", minimum_score: float = None,
                    cookies: Union[dict, list, str] = None) -> str:
        '''
        Create Recaptcha V3 task
        '''
        data = {
            "clientKey": self.client_key,
            "task": {
                "type": "ReCaptchaV3Task",
                "websiteURL": website_url,
                "websiteKey": website_key,
                "pageAction": page_action
            }
        }
        data, is_user_agent = self._add_user_agent(data)
        data, is_proxy = self._is_proxy_task(data)
        data = self._add_cookies(cookies, data)
        if minimum_score is not None:
            data["task"]["minScore"] = minimum_score
        return self._make_request(RequestType.CreateTask, data).get("taskId")