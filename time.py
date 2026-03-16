def time(timer: int) -> int:
    hours = timer // 60
    minutes = timer % 60
    return hours // 10 + hours % 10 + minutes // 10 + minutes % 10


print(time(240))
print(time(808))
