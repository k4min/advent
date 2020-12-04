import unittest

from advent.day3 import main


class TestToboggan(unittest.TestCase):

    def setUp(self):
        """Set up tests"""
        self.patterns = [
            '..##.......',
            '#...#...#..',
            '.#....#..#.',
            '..#.#...#.#',
            '.#...##..#.',
            '..#.##.....',
            '.#.#.#....#',
            '.#........#',
            '#.##...#...',
            '#...##....#',
            '.#..#...#.#'
        ]

    def test_main_basic(self):
        """Test the basic version"""
        expected = 7
        actual = main.count_trees(self.patterns)
        self.assertEqual(expected, actual)
