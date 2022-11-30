from capsolver_python import RecaptchaV2Task
from capsolver_python.utils import CapSolverException
import unittest


class BaseMethodTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cpt = RecaptchaV2Task("apikey")
        return super().setUp()

    def test_get_balance(self):
        try:
            balance = self.cpt.get_balance()
        except CapSolverException:
            self.fail("get_balance is failed!")
        self.assertTrue(balance is not None)

    def test_get_packages(self):
        try:
            packages = self.cpt.get_packages()
        except CapSolverException:
            self.fail("get_packages is failed!")
        self.assertTrue(packages is not None)
        

if __name__ == '__main__':
    unittest.main()