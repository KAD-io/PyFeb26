def test02_task06(file_path):

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        text = "".join(lines)

    line_count = len(lines)
    word_count = len(text.split())

    letter_count = sum(char.isalpha() for char in text)

    stats = (
        f"line count: {line_count}\n"
        f"word_count: {word_count}\n"
        f"word count: {letter_count}\n"
    )

    print(stats)

    with open(file_path, 'a', encoding='utf-8') as file:
        file.write(stats)


test02_task06('data.txt')
