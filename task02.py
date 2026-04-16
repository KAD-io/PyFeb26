def test02_task02_1():
    number = input("Input number: ")
    print(pow(int(number), 2))


def test02_task02_2():
    number = input("Input number: ")
    print(f'The number {number} is even: {not bool(int(number)%2)}')


test02_task02_1()
test02_task02_2()