import os


def _search_by_letter(row_string, range_length):
    """Search for position in a range."""
    current_range = (0, range_length - 1)
    for letter in row_string:
        # half the length of the range
        range_difference = int((current_range[1] - current_range[0]) / 2)
        if letter in ('F', 'L'):
            current_range = (current_range[0], current_range[0] + range_difference)
        if letter in ('B', 'R'):
            current_range = (current_range[0] + range_difference + 1, current_range[1])

    return current_range[0]


def get_seat(boarding_pass):
    """Given a row of FBFB... get the row, column for it."""
    row = boarding_pass[:7]
    column = boarding_pass[7:]
    return _search_by_letter(row, 128), _search_by_letter(column, 8)


def seat_id(seat_coordinates):
    """Given a tuple of row, column, get the 'seat id'"""
    x, y = seat_coordinates
    return x*8 + y


def find_missing_value(ids):
    """Given a list of IDs, find two that are two apart"""
    ids = sorted(ids)
    i = 0
    while i < len(ids) - 2:
        # They must be adjacent in a sorted list.  If not, then
        # an ID exists between them and the ticket we're looking
        # for is not missing
        i0 = ids[i]
        i1 = ids[i+1]
        if i1 - i0 == 2:
            return int((i0 + i1) / 2)
        i += 1


def max_id(data_lines):
    """Get the max seat id"""
    seats = [get_seat(p) for p in data_lines]
    return max(seat_id(seat) for seat in seats)


def my_seat_id(data_lines):
    seat_ids = [seat_id(get_seat(l)) for l in data_lines]
    return find_missing_value(seat_ids)


def main():
    """Main method"""
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file) as f:
        data = f.read()

    # part 1
    print(max_id(data.splitlines()))

    # part 2
    print(my_seat_id(data.splitlines()))


if __name__ == '__main__':
    main()
