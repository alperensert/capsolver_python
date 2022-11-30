from .capsolver import CapSolver


class UserAgent(CapSolver):
    def __init__(self, client_key, beta: bool = False):
        super().__init__(client_key, beta)
        self._user_agent = None

    def set_user_agent(self, user_agent: str):
        self._user_agent = user_agent

    def reset_user_agent(self):
        self._user_agent = None

    def _add_user_agent(self, data):
        if self._user_agent:
            data["task"]["userAgent"] = self._user_agent
            return data, True
        return data, False