"""nm11_job2"""


def is_number(func):
    def wrapper(*args):
        result = func(*args)
        if not isinstance(result, (int, float)):
            print(f"Error: The {func.__name__} function returned {type(result).__name__} "
                  "instead of a number.")
            return None
        return result
    return wrapper


@is_number
def nm11_job2(value):
    """
    If value is a number, it returns value, otherwise it returns None and outputs an error message
    """
    return value


assert nm11_job2(2) == 2
assert nm11_job2(2.2) == 2.2
assert nm11_job2('321') is None
