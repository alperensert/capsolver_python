from .proxy import Proxy
from .useragent import UserAgent
from .request_type import RequestType


class DataDomeSliderTask(UserAgent, Proxy):
    '''
    Class to solve Data dome slider tasks.

    This task type DatadomeSliderTask require that you send us your proxies.

    We support the following proxy types: SOCKS4, SOCKS5, HTTP, HTTPS with authentication by IP address or login and password. 

    If you want to use proxies by authentication by IP address, please add into the whitelist this ip: 47.253.53.46
    '''
    def __init__(self, client_key: str, beta: bool = False) -> None:
        super(DataDomeSliderTask, self).__init__(client_key, beta)

    def create_task(self, website_url: str, captcha_url: str) -> str:
        data = {
            "clientKey": self.client_key,
            "task": {
                "type": "DatadomeSliderTask",
                "websiteURL": website_url,
                "captchaUrl": captcha_url
            }
        }
        return self._make_request(RequestType.CreateTask, data).get("taskId")