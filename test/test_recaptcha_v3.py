from capsolver_python import RecaptchaV3Task
from capsolver_python.utils import CapSolverException
import unittest


class RecaptchaV3TaskTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cpt = RecaptchaV3Task("apikey")
        self.cookies = "cookiename1=cookievalue1;cookiename2=cookievalue2"
        self.task_id = None
        return super().setUp()

    def test_create_task(self):
        try:
            self.task_id = self.cpt.create_task("https://lessons.zennolab.com/captchas/recaptcha/v3.php?level=beta",
                "6Le0xVgUAAAAAIt20XEB4rVhYOODgTl00d8juDob", cookies=self.cookies)
        except CapSolverException:
            self.fail("recaptcha v3 create task is failed!")

if __name__ == '__main__':
    unittest.main()