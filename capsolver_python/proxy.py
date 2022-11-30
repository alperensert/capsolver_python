from .capsolver import CapSolver


class Proxy(CapSolver):
    def __init__(self, client_key, beta: bool = False):
        super().__init__(client_key, beta)
        self._proxy_type = None
        self._proxy_address = None
        self._proxy_port = None
        self._proxy_login = None
        self._proxy_password = None

    def set_proxy(self, proxy_type: str, proxy_address: str, proxy_port: int,
                  proxy_login: str = None, proxy_password: str = None):
        '''
        Available proxy types are: socks5 | https | http | socks4
        '''
        self._proxy_type = proxy_type
        self._proxy_address = proxy_address
        self._proxy_port = proxy_port
        self._proxy_login = proxy_login
        self._proxy_password = proxy_password

    def disable_proxy(self):
        self._proxy_type = None
        self._proxy_address = None
        self._proxy_port = None
        self._proxy_login = None
        self._proxy_password = None

    def _is_proxy_task(self, data: dict):
        """
        Determine for is this a proxy task or not?
        e.g if you are not set the values with set_proxy method, it is a proxyless method, or if you are set up it is a
        proxy task.
        """
        if self._proxy_type and self._proxy_address and self._proxy_port:
            data["task"]["proxyType"] = self._proxy_type
            data["task"]["proxyAddress"] = self._proxy_address
            data["task"]["proxyPort"] = self._proxy_port
            if self._proxy_login and self._proxy_password:
                data["task"]["proxyLogin"] = self._proxy_login
                data["task"]["proxyPassword"] = self._proxy_password
            return data, True
        data["task"]["type"] += "Proxyless"
        return data, False