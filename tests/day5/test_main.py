import unittest

from advent.day5 import main


class TestMain(unittest.TestCase):

    def test_get_one_seat(self):
        """Test the basic version"""
        row_string = 'FBFBBFFRLR'
        expected_seat = (44, 5)
        self.assertEqual(expected_seat, main.get_seat(row_string))

    def test_get_max_id(self):
        rows = [
            'BFFFBBFRRR',
            'FFFBBBFRRR',
            'BBFFBBFRLL'
        ]
        expected_max_id = 820
        self.assertEqual(expected_max_id, main.max_id(rows))

    def test_find_id(self):
        ids = [124, 127, 455, 457, 999]
        expected_id = 456
        self.assertEqual(expected_id, main.find_missing_value(ids))




