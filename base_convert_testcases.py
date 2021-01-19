import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):
    def test_base2(self):
        # normal test for base 2
        self.assertEqual(convert(45,2),"101101")

    def test_base4(self):
        # normal test for base 4
        self.assertEqual(convert(30,4),"132")

    def test_base16(self):
        # normal test for base 16
        self.assertEqual(convert(316,16),"13C")

        # full letter test for base 16
        self.assertEqual(convert(11259375,16),"ABCDEF")

if __name__ == "__main__":
        unittest.main()
