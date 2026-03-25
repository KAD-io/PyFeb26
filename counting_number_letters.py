"""hm10_job3"""


def get_number_letters(text: str) -> str:
    """
    :param text: the string is, for example, "cccbba"
    :return: the number of identical letters in a row in a row, for example, the string “c3b2a"
    """
    def add_result(add_count: int, add_char: str) -> str:
        return add_char + str(add_count) if add_count > 1 else add_char

    count = 0
    current_char = ''
    result = ''
    for char in text:
        if current_char == char:
            count += 1
        else:
            result += add_result(count, current_char)
            current_char = char
            count = 1

    return result + add_result(count, current_char)


assert get_number_letters("cccbba") == "c3b2a"
assert get_number_letters("abeehhhhhccced") == "abe2h5c3ed"
assert get_number_letters("aaabbceedd") == "a3b2ce2d2"
assert get_number_letters("abcde") == "abcde"
assert get_number_letters("aaabbdefffff") == "a3b2def5"
assert get_number_letters("") == ""
