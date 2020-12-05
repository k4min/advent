import os
import re

REQUIRED_FIELDS = {
    'byr': lambda x: _year_valid(x, 1920, 2002, 4),
    'iyr': lambda x: _year_valid(x, 2010, 2020, 4),
    'eyr': lambda x: _year_valid(x, 2020, 2030, 4),
    'hgt': lambda x: _height_valid(x),
    'hcl': lambda x: re.match('^#[0-9,a-f]{6}$', x),
    'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
    'pid': lambda x: len(x) == 9
}


def _height_valid(height):
    """Return is a height is within the given parameters

    Args:
        height: a string of digits with 'cm' or 'in' at the end
    """
    min_height_cm = 150
    max_height_cm = 193
    min_height_in = 59
    max_height_in = 76
    try:
        if height[-2:] == 'cm':
            return min_height_cm <= int(height[:-2]) <= max_height_cm
        if height[-2:] == 'in':
            return min_height_in <= int(height[:-2]) <= max_height_in
        return False
    except (IndexError, ValueError):
        return False


def _year_valid(year, lower, upper, length):
    """Check if a year is valid

    Args:
        year: a string of a year
        lower: lower bound
        upper: upper bound
        length: length of the number
    """
    try:
        return lower <= int(year) <= upper and len(year) == length
    except ValueError:
        return False


def passport_has_required_fields(passport):
    """Check if an individual passport is legal

    Args:
        passport: a string describing a single passport
    Returns:
        True if the passport is valid
    """
    values = dict([p.split(':') for p in passport.split()])
    return all(p in values for p in REQUIRED_FIELDS)


def passport_fields_are_valid(passport):
    """Check if a passport passes the validation tests

    Args:
        passport: a string describing a single passport
    Returns:
        True if the passport is valid

    """
    values = dict([p.split(':') for p in passport.split()])
    return all(REQUIRED_FIELDS.get(k, lambda x: True)(v) for (k, v) in values.items())


def valid_passports_part1(data):
    """Do day4 part1

    Args:
        data: A multi-line string containing the contents of the input file

    Returns:
        The number of valid passports
    """
    passports = data.split('\n\n')
    return [p for p in passports if passport_has_required_fields(p)]


def valid_passports_part2(data):
    """Do day4 part2

    Args:
        data: A multi-line string containing the contents of the input file

    Returns:
        The number of valid passports
    """
    valid_passports = valid_passports_part1(data)
    return [p for p in valid_passports if passport_fields_are_valid(p)]


def main():
    """Main method"""
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file) as f:
        data = f.read()

    # part 1
    print(len(valid_passports_part1(data)))

    # part 2
    print(len(valid_passports_part2(data)))


if __name__ == '__main__':
    main()
