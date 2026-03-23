"""hm9 job2"""


def get_number_opposite(n: int, first_number: int) -> int:
    """
    :param n: the number of digits in the dial from 0 to n-1
    :param first_number: position in the dial
    :return: the number that is written in the radially opposite position from "first_number"
             or -1 if the parameters "n" and "first_number" are incorrect
    """
    if not isinstance(n, int) or not isinstance(first_number, int):
        return -1
    else:
        if n % 2 or first_number > n - 1 or n < 2 or first_number < 0:
            return -1
    return first_number - int(n/2) if first_number >= n/2 else first_number + int(n/2)


assert get_number_opposite(10, 6) == 1
assert get_number_opposite(10, 2) == 7
assert get_number_opposite(10, 4) == 9
