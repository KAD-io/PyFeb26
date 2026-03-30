"""nm11_job3"""


def typed(type_):
    """
    decorator typed converts arguments to the desired type and summarizes
    """
    def decorator(func):
        def wrapper(*args):
            conv_args = [type_(arg) for arg in args]
            return func(*conv_args)
        return wrapper
    return decorator


@typed(type_=str)
def add1(a, b):
    return a + b


assert add1("3", 5) == "35"
assert add1(5, 5) == "55"
assert add1('a', 'b') == 'ab'


@typed(type_=int)
def add2(a, b, c):
    return a + b + c


assert add2(5, 6, 7) == 18


@typed(type_=float)
def add3(a, b, c):
    return a + b + c


assert add3(0.1, 0.2, 0.4) == 0.7000000000000001
