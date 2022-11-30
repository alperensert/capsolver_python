from .capsolver import CapSolver
from .request_type import RequestType


class AntiAkamaiBMPTask(CapSolver):
    '''
    Class to solve AntiAkamaiBMP tasks.

    Only IOS sensor is supported, and you'll need to implement the tls by yourself
    '''
    def __init__(self, client_key: str, beta: bool = False) -> None:
        super(AntiAkamaiBMPTask, self).__init__(client_key, beta)

    def create_task(self, package_name: str, version: str = None, device_id: str = None,
                    device_name: str = None, count: int =  None) -> str:
        data = {
            "clientKey": self.client_key,
            "task": {
                "type": "AntiAkamaiBMPTask",
                "packageName": package_name
            }
        }
        if version is not None:
            data["task"]["version"] = version
        if device_id is not None:
            data["task"]["deviceId"] = device_id
        if device_name is not None:
            data["task"]["deviceName"] = device_name
        if count is not None:
            data["task"]["count"] = count
        return self._make_request(RequestType.CreateTaskAntiAkamai, data).get("taskId")