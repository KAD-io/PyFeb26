def test02_task05(number=10201):
    if number < 0:
        return False
    str_number = str(number)
    str_number_01 = str_number[0:len(str_number)//2]
    if len(str_number) % 2:
        str_number_02 = str_number[len(str_number)//2+1:len(str_number)]
    else:
        str_number_02 = str_number[len(str_number) // 2:len(str_number)]
    return str_number_01 == str_number_02[::-1]


test02_task05()