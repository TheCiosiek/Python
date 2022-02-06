import unittest
from zadanie_10 import check_date

class Tests(unittest.TestCase):
    def testCheckDate(self):
        self.assertEqual(check_date("05/21"),True)
        self.assertEqual(check_date("5/21"),True)
        self.assertEqual(check_date("5/01"),True)
        self.assertEqual(check_date("11/0"),False)
        self.assertEqual(check_date("-5/15"),False)
        self.assertEqual(check_date("110"),False)
        self.assertEqual(check_date("/"),False)
        self.assertEqual(check_date(" / "),False)

unittest.main()
