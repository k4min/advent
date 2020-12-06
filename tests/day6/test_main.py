from textwrap import dedent
import unittest

from advent.day6 import main


class TestMain(unittest.TestCase):

    def setUp(self):
        """Set up tests"""
        self.data = dedent(
            '''
            abc
    
            a
            b
            c
    
            ab
            ac
    
            a
            a
            a
            a
    
            b
            '''
        )

    def test_sum_groups(self):
        expected = 11
        actual = main.sum_groups(self.data)
        self.assertEqual(expected, actual)

    def test_sum_groups_all_answered(self):
        expected = 6
        actual = main.sum_groups_all_answered(self.data)
        self.assertEqual(expected, actual)
