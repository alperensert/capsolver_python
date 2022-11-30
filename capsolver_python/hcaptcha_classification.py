from .capsolver import CapSolver
from .request_type import RequestType


class HCaptchaClassificationTask(CapSolver):
    '''
    Class to solve HCaptcha classification tasks.
    '''
    def __init__(self, client_key: str, beta: bool = False) -> None:
        super(HCaptchaClassificationTask, self).__init__(client_key, beta)

    def create_task(self, queries: list, question: str, coordinate: bool = None) -> str:
        data = {
            "clientKey": self.client_key,
            "task": {
                "type": "HCaptchaClassification",
                "queries": queries,
                "question": question
            }
        }
        if coordinate is not None:
            data["task"]["coordinate"] = coordinate
        return self._make_request(RequestType.CreateTask, data).get("taskId")