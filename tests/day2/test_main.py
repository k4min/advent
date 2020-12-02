import unittest
from advent.day2 import main


class TestPolicy(unittest.TestCase):

    def setUp(self):
        self.example_input = [
            '1-3 a: abcde',
            '1-3 b: cdefg',
            '2-9 c: ccccccccc'
        ]

    def test_line_is_valid(self):
        self.assertEqual(main.valid_lines(self.example_input, main._line_is_valid), 2)

    def test_line_is_valid_part_2(self):
        self.assertEqual(main.valid_lines(self.example_input, main._line_is_valid_part2), 1)
