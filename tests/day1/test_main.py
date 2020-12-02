import unittest
from advent.day1 import main


class TestSum(unittest.TestCase):

    def setUp(self):
        # In this example, 1721 + 299 = 2020, so the expected result is 1721 * 299 = 514579
        self.example_data = [
            1721,
            979,
            366,
            299,
            675,
            1456,
        ]
        self.expected_result = 514579

    def testBasic(self):
        """Test the basic version of this works"""
        self.assertEqual(main.multiply_sum(self.example_data), self.expected_result)

    def testWithSameDups(self):
        """A list that has more than one of the same number should still work"""
        self.example_data.append(1721)
        self.assertEqual(main.multiply_sum(self.example_data), self.expected_result)

    def testEvenDivision(self):
        """Test that having one instance of 2020/2 does not work"""
        self.example_data = [1010]
        self.assertIsNone(main.multiply_sum(self.example_data))


class Test3WaySum(unittest.TestCase):

    def setUp(self):
        # In this example, 1721 + 299 = 2020, so the expected result is 1721 * 299 = 514579
        self.example_data = [
            1721,
            979,
            366,
            299,
            675,
            1456,
        ]
        self.expected_result = 241861950

    def testBasic(self):
        """Test the basic version of this works"""
        self.assertEqual(main.multiply_3_way_sum(self.example_data), self.expected_result)