from .capsolver import CapSolver
from .request_type import RequestType


class FunCaptchaClassificationTask(CapSolver):
    '''
    Class to solve FunCaptcha classification tasks.

    This task type FunCaptchaClassification use our own proxies servers.
    '''
    def __init__(self, client_key: str, beta: bool = False) -> None:
        super(FunCaptchaClassificationTask, self).__init__(client_key, beta)

    def create_task(self, image: str, question: str) -> str:
        data = {
            "clientKey": self.client_key,
            "task": {
                "type": "FunCaptchaClassification",
                "image": image,
                "question": question
            }
        }
        return self._make_request(RequestType.CreateTask, data).get("taskId")