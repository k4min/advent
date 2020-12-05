from textwrap import dedent
import unittest

from advent.day4 import main


class TestMain(unittest.TestCase):

    def setUp(self):
        """Set up tests"""
        self.input_contents = dedent(
            '''
            ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
            byr:1937 iyr:2017 cid:147 hgt:183cm
  
            iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
            hcl:#cfa07d byr:1929

            hcl:#ae17e1 iyr:2013
            eyr:2024
            ecl:brn pid:760753108 byr:1931
            hgt:179cm

            hcl:#cfa07d eyr:2025 pid:166559648
            iyr:2011 ecl:brn hgt:59in
            '''
        )

    def test_main_basic_part1(self):
        """Test the basic version of part1"""
        expected = 2
        actual = len(main.valid_passports_part1(self.input_contents))
        self.assertEqual(expected, actual)

    def test_main_basic_part2(self):
        """Test the basic version of part2"""
        expected = 2
        actual = len(main.valid_passports_part2(self.input_contents))
        self.assertEqual(expected, actual)

    def test_passport_is_legal(self):
        """Test all fields present on a single passport"""
        passport = dedent(
            '''
            ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
            byr:1937 iyr:2017 cid:147 hgt:183cm
            '''
        )
        self.assertTrue(main.passport_has_required_fields(passport))

    def test_passport_has_valid_fields(self):
        """Test all fields are correct on a single passport"""
        passport = dedent(
            '''
            ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
            byr:1937 iyr:2017 cid:147 hgt:183cm
            '''
        )
        self.assertTrue(main.passport_fields_are_valid(passport))

    def test_other_passport_has_valid_fields(self):
        passport = dedent(
            '''
            hcl:#cfa07d eyr:2025 pid:166559648
            iyr:2011 ecl:brn hgt:59in
            '''
        )
        self.assertTrue(main.passport_fields_are_valid(passport))

    def test_passport_bad_ecl(self):
        """Test when ecl is not valid"""
        passport = dedent(
            '''
            ecl:beef pid:860033327 eyr:2020 hcl:#fffffd
            byr:1937 iyr:2017 cid:147 hgt:183cm
            '''
        )
        self.assertFalse(main.passport_fields_are_valid(passport))

    def test_passport_bad_byr(self):
        """Test when byr is not valid"""
        passport = dedent(
            '''
            ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
            byr:beef iyr:2017 cid:147 hgt:183cm
            '''
        )
        self.assertFalse(main.passport_fields_are_valid(passport))

    def test_passport_bad_pid(self):
        """Test when pid is not valid"""
        passport = dedent(
            '''
            ecl:gry pid:86033aaa033327 eyr:2020 hcl:#fffffd
            byr:1937 iyr:2017 cid:147 hgt:183cm
            '''
        )
        self.assertFalse(main.passport_fields_are_valid(passport))

    def test_passport_bad_hcl(self):
        """Test when hcl is not valid"""
        passport = dedent(
            '''
            ecl:gry pid:860033327 eyr:2020 hcl:#fffyyyffd
            byr:1937 iyr:2017 cid:147 hgt:183cm
            '''
        )
        self.assertFalse(main.passport_fields_are_valid(passport))

    def test_passport_bad_hgt(self):
        """Test when hgt is not valid"""
        passport = dedent(
            '''
            ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
            byr:1937 iyr:2017 cid:147 hgt:183kg
            '''
        )
        self.assertFalse(main.passport_fields_are_valid(passport))





