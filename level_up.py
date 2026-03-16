def level_up(experience: int, threshold: int, reward: int) -> bool:
    return experience + reward >= threshold


print(level_up(10, 15, 5))
print(level_up(10, 15, 4))
