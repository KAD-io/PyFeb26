"""hm10_job2"""


def candles(candle_number: int, make_new: int) -> int:
    """
    :param candle_number: the number of candles that are available initially
    :param make_new: the number of stubs required to create a new candle
    :return: the total number of candles that can be burned
    """
    candle_sum = candle_number
    while candle_number >= make_new:
        candle_new = candle_number // make_new
        candle_sum += candle_new
        candle_number = candle_new + candle_number % make_new
    return candle_sum


assert candles(5, 2) == 9
assert candles(1, 2) == 1
assert candles(15, 5) == 18
assert candles(12, 2) == 23
assert candles(6, 4) == 7
assert candles(13, 5) == 16
assert candles(2, 3) == 2
