"""hm14_job1"""

import random


class Student:
    def __init__(self, name, group, estimation):
        self.name = name
        self.group = group
        self.estimation = estimation

    def to_str(self):
        return f"{self.name};{self.group};{self.estimation}"

    @classmethod
    def from_str(cls, student_str):
        student_info = student_str.split(';')
        try:
            return cls(student_info[0], student_info[1], int(student_info[2]))
        except IndexError:
            return IndexError
        except ValueError:
            return ValueError


def create_list_students():
    names = [
        "Астафьева Ивона",
        "Новик Полина",
        "Дмуховский Артемий",
        "Сирота Андрей",
        "Овсянникова Юлия",
        "Кривогин Андрей",
        "Трушинский Артур",
        "Янченко Артур",
        "Шмаргун Сергей",
        "Клюев Руслан",
        "Шмаргун Сергей",
        "Кривогин Андрей",
    ]

    group_prefix = "Md-PT2-22-"

    students = []
    for name in names:
        students.append(Student(name,
                                group_prefix+str(random.randint(25, 27)),
                                random.randint(8, 10)))

    return students


def write_file(file_name):
    students_list = create_list_students()
    with open(file_name, "w", encoding="utf-8") as file:
        file.writelines(student.to_str() + '\n' for student in students_list)


def edit_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            students_list_str = file.readlines()

        students_list = [Student.from_str(students_line.strip())
                         for students_line in students_list_str]
        if IndexError in students_list or ValueError in students_list:
            print(f"Error: Incorrect list of students in the file {file_name}")
            return None

        dict_group = {}
        for student in students_list:
            if student.group in dict_group:
                dict_group[student.group]['number'] += 1
                dict_group[student.group]['avg'] += student.estimation
            else:
                dict_group[student.group] = {}
                dict_group[student.group]['number'] = 1
                dict_group[student.group]['avg'] = student.estimation

        for _, data in dict_group.items():
            data['avg'] /= data['number']

        with open(file_name, "a", encoding="utf-8") as file:
            file.write(f"\nTotal number of students: {len(students_list)}\n")
            file.write("\nThe number of students and the average grade for each group:\n")
            for group, info in dict_group.items():
                file.write(f"Group: {group}\t"
                           f"Number of students: {info['number']}\t"
                           f"AVG: {round(info['avg'],2)}\n")

    except FileNotFoundError:
        print(f"Error: File {file_name} not found.")


write_file("students.txt")
edit_file("students.txt")
