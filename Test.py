import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 10, "Should be 10")

    def test_sum_tuple(self):
        self.assertEqual(sum((3, 2, 5)), 10, "Should be 10")

if __name__ == '__main__':
    unittest.main()
    