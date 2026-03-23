"""hm9 job1"""


def is_strictly_increasing(sequence: list[int]) -> bool:
    """
    Determines whether the "sequence" is strictly ascending
    """
    return all(sequence[i] < sequence[i+1] for i in range(len(sequence)-1))


def is_possible_get_strictly_increasing_list(sequence: list[int]) -> bool:
    """
    Determines whether it is possible to obtain a strictly increasing "sequence"
    by deleting no more than one element from the array.
    """
    if not all(isinstance(x, int) for x in sequence):
        return False
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1]:
            return (is_strictly_increasing(sequence[:i] + sequence[i+1:]) or
                    is_strictly_increasing(sequence[:i+1] + sequence[i+2:]))
    return True


assert is_possible_get_strictly_increasing_list([1, 2, 3])
assert not is_possible_get_strictly_increasing_list([1, 2, 1, 2])
assert not is_possible_get_strictly_increasing_list([1, 3, 2, 1])
assert not is_possible_get_strictly_increasing_list([1, 2, 3, 4, 5, 3, 5, 6])
assert not is_possible_get_strictly_increasing_list([40, 50, 60, 10, 20, 30])
