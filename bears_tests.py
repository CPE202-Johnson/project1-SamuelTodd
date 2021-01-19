import unittest
from bears import *

class TestAssign1(unittest.TestCase):
    def test_bear_01(self):
        # test for bears requiring multiple steps
        self.assertTrue(bears(250))

    def test_bear_02(self):
        # test for starting with correct # of bears
        self.assertTrue(bears(42))

    def test_bear_03(self):
        # test for false requiring steps
        self.assertFalse(bears(53))

    def test_bear_04(self):
        # test for false with too few bears
        self.assertFalse(bears(41))

if __name__ == "__main__":
    unittest.main()
