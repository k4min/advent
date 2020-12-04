# day 1: https://adventofcode.com/2020/day/1
import os

def multiply_sum(values):
    """Find two values in a list of ints that add up to 2020, and return their product"""
    for v1 in values:
        for v2 in values:
            if v1 == v2:
                continue
            if v1 + v2 == 2020:
                return v1*v2


def multiply_3_way_sum(values):
    """Find three values in a list of ints that add up to 2020, and return their product"""
    for v1 in values:
        for v2 in values:
            if v1 == v2:
                continue
            for v3 in values:
                if v3 in (v1, v2):
                    continue
                if v1 + v2 + v3 == 2020:
                    return v1*v2*v3


def main():
    """Main method"""

    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file) as f:
        data = [int(s) for s in f.read().split()]

    # part 1:
    print(multiply_sum(data))

    # part 2:
    print(multiply_3_way_sum(data))


if __name__ == '__main__':
    main()
