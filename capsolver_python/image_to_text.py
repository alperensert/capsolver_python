from .capsolver import CapSolver
from .utils import CapSolverException
from .request_type import RequestType
from base64 import b64encode


class ImageToTextTask(CapSolver):
    '''
    Class to solve Image to text tasks.
    '''
    def __init__(self, client_key: str, beta: bool = False) -> None:
        super(ImageToTextTask, self).__init__(client_key, beta)

    def create_task(self, image_path: str = None, base64_encoded_image: str = None) -> str:
        '''
        Create Image to text task
        '''
        if base64_encoded_image is None and image_path is None:
            raise CapSolverException(error_id=-1,
                                      error_code="ERROR_NOTHING_GIVEN",
                                      error_description="You have to give image_path or base64_encoded_image")
        data = {
            "clientKey": self.client_key,
            "task": {
                "type": "ImageToTextTask"
            }
        }
        if base64_encoded_image is None:
            img_body = self._from_path(image_path)
            data["task"]["body"] = img_body
        else:
            data["task"]["body"] = base64_encoded_image
        return self._make_request(RequestType.CreateTask, data).get("taskId")

    @staticmethod
    def _from_path(image_path: str):
        with open(image_path, "rb") as img:
            base64_img = b64encode(img.read()).decode("ascii")
        return base64_img