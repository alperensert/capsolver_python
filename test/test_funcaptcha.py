from capsolver_python import FunCaptchaTask
from capsolver_python.utils import CapSolverException
import unittest


class FunCaptchaTaskTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cpt = FunCaptchaTask("apikey")
        self.task_id = None
        return super().setUp()

    def test_create_task(self):
        try:
            self.task_id = self.cpt.create_task("https://funcaptcha.com/fc/api/nojs/?pkey=69A21A01-CC7B-B9C6-0F9A-E7FA06677FFC",
                "69A21A01-CC7B-B9C6-0F9A-E7FA06677FFC", "https://funcaptcha.com")
        except CapSolverException:
            self.fail("funcaptchatask create task is failed!")

if __name__ == '__main__':
    unittest.main()