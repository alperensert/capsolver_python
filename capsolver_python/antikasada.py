from .proxy import Proxy
from .useragent import UserAgent
from .request_type import RequestType


class AntiKasadaTask(UserAgent, Proxy):
    '''
    Class to solve AntiKasada tasks.

    This task type AntiKasadaTask require that you send us your proxies.

    We support the following proxy types: SOCKS4, SOCKS5, HTTP, HTTPS with authentication by IP address or login and password. 

    If you want to use proxies by authentication by IP address, please add into the whitelist this ip: 47.253.53.46
    '''
    def __init__(self, client_key: str, beta: bool = False) -> None:
        super(AntiKasadaTask, self).__init__(client_key, beta)

    def create_task(self, page_url: str, only_cd: str = None) -> str:
        data = {
            "clientKey": self.client_key,
            "task": {
                "pageURL": page_url
            }
        }
        if only_cd is not None:
            data["task"]["onlyCD"] = only_cd
        return self._make_request(RequestType.CreateTaskKasada, data).get("taskId")