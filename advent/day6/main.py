from functools import reduce
import os


def get_group_answers(group):
    """Given a string representing a group return unique letters in it"""
    group_answers = set()
    for passenger in group.split():
        group_answers = group_answers.union(set([letter for letter in passenger]))
    return group_answers


def get_group_all_answers(group):
    """Given a string representing a group return letters which are on every line"""
    # create a list of sets for each line in the group
    group_answers = [set(let for let in letters) for letters in group.split()]
    group_answers = reduce(set.intersection, group_answers)
    return group_answers


def sum_groups(groups):
    """For a string of group data, get the sum of unique answers in each group"""
    groups = groups.split('\n\n')
    return sum(len(get_group_answers(g)) for g in groups)


def sum_groups_all_answered(groups):
    """For a string of group data, get the sum of answers which exist for each member of each group"""
    groups = groups.split('\n\n')
    return sum(len(get_group_all_answers(g)) for g in groups)


def main():
    """Main method"""
    input_file = os.path.join(os.path.dirname(__file__), 'input')
    with open(input_file) as f:
        data = f.read()

    # part 1
    print(sum_groups(data))

    # part 2
    print(sum_groups_all_answered(data))


if __name__ == '__main__':
    main()
