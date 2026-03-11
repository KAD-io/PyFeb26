def hm6():
    # job 1. 
    # Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
    str_job1 = 'www.my_site.com#about'
    print(str_job1.replace('#', '/'))

    # job 2. 
    # Напишите программу, которая добавляет ‘ing’ к словам
    str_job2 = 'test'
    print(str_job2 + 'ing')

    # job 3. 
    # В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
    str_job3 = 'Ivanou Ivan'
    print(str_job3[str_job3.find(' ') + 1:len(str_job3)] + ' ' + str_job3[0:str_job3.find(' ')])

    # job 4. 
    # Напишите программу которая удаляет пробел в начале, в конце строки
    str_job4 = '   test   '
    print(str_job4.strip())

    # job 5. 
    # Имена собственные всегда начинаются с заглавной буквы, за которой следуют строчные буквы.
    # Исправьте данное имя собственное так, чтобы оно соответствовало этому утверждению. 
    # "pARiS" >> "Paris"
    str_job5 = 'pARiS'
    print(str_job5.title())

    # job 6. 
    # Перевести строку в список "Robin Singh" => ["Robin”, “Singh"],
    # "I love arrays they are my favorite" => 
    # ["I", "love", "arrays", "they", "are", "my", "favorite"]
    str_job6_1 = "Robin Singh"
    str_job6_2 = "I love arrays they are my favorite"
    print(str_job6_1.split())
    print(str_job6_2.split())

    # job 7. Дан список: [Robin Singh], и 2 строки: "Welcome" и "airport".
    # Напечатайте текст: “Hello, Robin Singh! Welcome to airport”
    list_job7 = ["Robin", "Singh"]
    str_job7_1 = "Welcome"
    str_job7_2 = "airport"
    print(f'Hello, {list_job7[0]} {list_job7[1]}! {str_job7_1} to {str_job7_2}')

    # job 8. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
    # сделайте из него строку => "I love arrays they are my favorite"
    list_job8 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
    print(" ".join(list_job8))

    # job 9. Создайте список из 10 элементов,
    # вставьте на 3-ю позицию новое значение,
    # удалите элемент из списка под индексом 6
    list_job9 = list(range(1, 11))
    list_job9.insert(2, "new")
    del list_job9[6]
    print(list_job9)


hm6()
