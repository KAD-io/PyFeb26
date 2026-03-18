"""hm8_job2"""


def is_infinity_loop(a: int, b: int) -> bool:
    """
    :return: Determines whether the following pseudocode leads to an infinite loop.
    Until 'a' is equal to 'b', Increase 'a' by 1, Decrease 'b' by 1
    """
    if a > b:
        return True
    return bool((a - b) % 2)


print(is_infinity_loop(2, 6))
print(is_infinity_loop(2, 3))
