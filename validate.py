"""hm9 job3"""


def is_validate(number: int) -> bool:
    """
    :param number: credit card number
    :return: the result of checking the "number" using the Luhn algorithm
    """
    if not isinstance(number, int):
        return False
    else:
        if number <= 0:
            return False
    number_list = [int(digit) for digit in str(number)]
    if not (8 <= len(number_list) <= 19):
        return False
    number_list.reverse()
    for i in range(len(number_list)):
        if i % 2:
            number_list[i] = number_list[i] * 2 - 9 if number_list[i] * 2 > 9 \
                else number_list[i] * 2
    return not bool(sum(number_list) % 10)


assert not is_validate(4561261212345464)
assert is_validate(30569309025904)
assert is_validate(5610591081018250)
assert is_validate(378734493671000)
assert is_validate(371449635398431)
assert is_validate(378282246310005)
