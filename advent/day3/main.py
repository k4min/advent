from functools import reduce
import operator
import os


def count_trees(lines, right=3, down=1):
    """Do day 3

    Args:
        lines: a list of strings describing the patterns
        right: how many spaces to move to the right
        down: how many spaces to move down
    """
    horizontal_index = right
    trees = 0
    # assume pattern length is uniform
    pattern_length = len(lines[0])
    # skip the first line(s)
    for i in range(down, len(lines), down):
        line = lines[i]
        cur_char = line[horizontal_index % pattern_length]
        if cur_char == '#':
            trees += 1
        horizontal_index += right

    return trees


def main():
    """Main method"""
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file) as f:
        data = f.read().splitlines()

    # part 1
    print(count_trees(data))

    # part 2
    part2_answers = [
        count_trees(data, 1, 1),
        count_trees(data, 3, 1),
        count_trees(data, 5, 1),
        count_trees(data, 7, 1),
        count_trees(data, 1, 2)
    ]

    print(reduce(operator.mul, part2_answers, 1))

if __name__ == '__main__':
    main()
