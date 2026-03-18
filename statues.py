"""hm8_job3"""


def get_count_missing_statues(statues: list[int]) -> int:
    """
    :param statues: list of statue sizes
    :return: number of missing statues
    """
    statues.sort()
    return sum(statues[i+1] - statues[i] - 1
               for i in range(len(statues)-1)
               if statues[i+1] - statues[i] != 1)


print(get_count_missing_statues([6, 2, 3, 8]))
