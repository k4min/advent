# day 2:
import re
import os


def _line_is_valid(line, policy_regex):
    """Given a line and a regex, determine if it's valid"""
    match = policy_regex.match(line)
    if not match:
        raise ValueError(f'Got an invalid line: {line}')
    min_letters = int(match.group(1))
    max_letters = int(match.group(2))
    letter = match.group(3)
    password_letters = [c for c in match.group(4)]
    num_letters = password_letters.count(letter)
    if min_letters <= num_letters <= max_letters:
        return True
    return False


def _line_is_valid_part2(line, policy_regex):
    """Given a line and a regex, determine if it's valid"""
    match = policy_regex.match(line)
    if not match:
        raise ValueError(f'Got an invalid line: {line}')
    position_1 = int(match.group(1)) - 1
    position_2 = int(match.group(2)) - 1
    letter = match.group(3)
    password = match.group(4)
    if password[position_1] == letter and password[position_2] != letter:
        return True
    if password[position_2] == letter and password[position_1] != letter:
        return True

    return False


def valid_lines(input_lines, validation_fn):
    """Given a list of passwords and policies, return the number of password lines that are valid"""
    # doesn't handle special characters
    policy_regex = re.compile('^(\d+)-(\d+) (\w): (\w+)$')
    return len([line for line in input_lines if validation_fn(line, policy_regex)])


def main():
    """Main method"""
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file) as f:
        data = f.read().splitlines()

    # part1
    print(valid_lines(data, _line_is_valid))

    # part2
    print(valid_lines(data, _line_is_valid_part2))


if __name__ == '__main__':
    main()
