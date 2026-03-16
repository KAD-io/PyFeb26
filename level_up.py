"""job 2."""
def is_level_up(experience: int, threshold: int, reward: int) -> bool:
    """
    :param experience: current XP
    :param threshold: threshold for level up
    :param reward: reward for killing monsters
    :return: will there be level up after killing the monster
    """
    return experience + reward >= threshold


print(is_level_up(10, 15, 5))
print(is_level_up(10, 15, 4))
