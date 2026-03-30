"""nm11_job1"""


def validate_arguments(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError(f"The argument {arg} must be positive number.")
        return func(*args)
    return wrapper


@validate_arguments
def nm11_job1(*args):
    """
    return: args
    If a negative argument is encountered, a ValueError is called.
    """
    return args


assert nm11_job1(1, 2, 3) == (1, 2, 3)
try:
    nm11_job1(1, -2, 3)
    assert False
except ValueError:
    pass
