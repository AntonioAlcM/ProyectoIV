import unittest

from sarao import Sarao


class Sarao_Test(unittest.TestCase):
    def setUp(self):
        self.sarao = Sarao()

    def get_name_test(self):
        self.assertIsInstance(self.sarao.get_name, list, "No es una lista")


if __name__ == '__main__':
    unittest.main()
