from .request_type import RequestType
from .proxy import *
from .useragent import *


class FunCaptchaTask(UserAgent, Proxy):
    '''
    Class to solve FunCaptcha tasks with or without proxy.
    '''
    def __init__(self, client_key: str, beta: bool = False) -> None:
        super(FunCaptchaTask, self).__init__(client_key, beta)

    def create_task(self, website_url: str,
                    website_public_key: str, api_js_subdomain: str,
                    data_blob: str = None) -> str:
        '''
        Create FunCaptcha task
        '''
        data = {
            "clientKey": self.client_key,
            "task": {
                "type": "FunCaptchaTask",
                "websiteURL": website_url,
                "websitePublicKey": website_public_key,
                "funcaptchaApiJSSubdomain": api_js_subdomain
            }
        }
        data, is_user_agent = self._add_user_agent(data)
        data, is_proxy = self._is_proxy_task(data)
        if data_blob is not None:
            data["task"]["data"] = data_blob
        return self._make_request(RequestType.CreateTask, data).get("taskId")