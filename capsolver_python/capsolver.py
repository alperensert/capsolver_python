import asyncio
import requests
from time import sleep
from .request_type import RequestType
from .utils import CapSolverException

class CapSolver:
    _HOST_URL = "https://api.capsolver.com"
    _BETA_HOST_URL = "https://api-beta.capsolver.com"

    def __init__(self, client_key: str, beta: bool = False) -> None:
        self.client_key = client_key
        self.beta = beta
    
    def get_balance(self) -> float:
        '''
        Returns balance for API key.
        '''
        data = {"clientKey": self.client_key}
        return self._make_request(RequestType.GetBalance, data).get("balance")
    
    def get_packages(self) -> list:
        '''
        Returns a list of monthly packages.
        '''
        data = {"clientKey": self.client_key}
        return self._make_request(RequestType.GetBalance, data).get("packages")

    def get_task_result(self, task_id: str):
        data = {
            "clientKey": self.client_key,
            "taskId": task_id
        }
        task_result = self._make_request(RequestType.GetTaskResult, data)
        return self._is_ready(task_result)
    
    def join_task_result(self, task_id: str, maximum_time: int = 90):
        for i in range(0, maximum_time + 1, 1):
            result = self.get_task_result(task_id)
            if result is not False and result is not None:
                return result
            elif result is False:
                i += 1
                sleep(1)
        raise CapSolverException(61, "ERROR_MAXIMUM_TIME_EXCEED", "Maximum time is exceed.")

    async def join_task_result_async(self, task_id: str, maximum_time: int = 90):
        for i in range(0, maximum_time + 1, 1):
            result = self.get_task_result(task_id)
            if result is not False and result is not None:
                return result
            elif result is False:
                i += 1
                await asyncio.sleep(1)
        raise CapSolverException(61, "ERROR_MAXIMUM_TIME_EXCEED", "Maximum time is exceed.")

    # TODO: Get a soft id for this one
    def _make_request(self, method: RequestType, data: dict):
        if method == RequestType.CreateTask or method == RequestType.CreateTaskAntiAkamai or method == RequestType.CreateTaskKasada:
            data["appId"] = "0C39FC4D-C1FB-4F4E-975B-89E93B78A97A"
        try:
            response = requests.post("{}{}".format(self._BETA_HOST_URL if self.beta else self._HOST_URL, method), json=data).json()
        except Exception as err:
            raise CapSolverException(-1, type(err).__name__, str(err))
        return response

    @staticmethod
    def _is_ready(response: dict):
        status = response.get("status")
        if status == "ready" or status == "processing":
            return False if status == "processing" else response.get("solution")
        else:
            raise CapSolverException(response.get("errorId"), response.get("errorCode"), response.get("errorDescription"))
    
    @staticmethod
    def _add_cookies(cookies, data):
        if cookies is None:
            return data
        str_cookies = ""
        if type(cookies) == dict:
            for key, value in cookies.items():
                if value == list(cookies.items())[-1][1]:
                    str_cookies += "{}={}".format(key, value)
                else:
                    str_cookies += "{}={};".format(key, value)
        elif type(cookies) == list:
            for i in cookies:
                if not len(cookies) % 2 == 0:
                    raise AttributeError("List cookies length must be even numbers")
                if cookies.index(i) % 2 == 0:
                    str_cookies += "{}=".format(i)
                elif cookies[cookies.index(i)] == cookies[-1]:
                    str_cookies += "{}".format(i)
                elif cookies.index(i) % 2 == 1:
                    str_cookies += "{};".format(i)
        elif type(cookies) == str:
            data["task"]["cookies"] = cookies
            return data
        data["task"]["cookies"] = str_cookies
        return data