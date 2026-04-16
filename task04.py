def test02_task04(list_numbers=[1, 2, 3]):
    r = 1
    number = 0
    for x in list_numbers[::-1]:
        number += x*r
        r *= 10

    number += 1

    new_list_numbers = []
    for i in str(number):
        new_list_numbers.append(i)

    print(f'rezult: {new_list_numbers}')


test02_task04()
