def time_converter(time24: str) -> str:
    hours24, minutes = time24.split(':')
    meridiem = 'a.m.' if int(hours24) < 12 else 'p.m.'
    hours12 = int(hours24) % 12 if int(hours24) % 12 != 0 else 12
    return f'{hours12}:{minutes} {meridiem}'


print(time_converter('12:30'))
print(time_converter('09:00'))
print(time_converter('23:15'))
print(time_converter('00:00'))
