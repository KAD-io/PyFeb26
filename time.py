def time(timer: int) -> int:
    """
    :param timer: minutes
    :return: the sum of the digits shown by the digital timer in the hh:mm format.
    """
    hours = timer // 60
    minutes = timer % 60
    return hours // 10 + hours % 10 + minutes // 10 + minutes % 10


print(time(240))
print(time(808))
