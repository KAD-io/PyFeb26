"""hm10_job1"""


def edit_str(text: str) -> str:
    """
    :param text: string
    :return: edited text where the "#" characters and characters in front of them are removed
    """
    while '#' in text:
        ind = text.find('#')
        text = text[:ind - 1] + text[ind + 1:] if ind else text[ind + 1:]
    return text


assert edit_str("a#bc#d") == "bd"
assert edit_str("abc#d##c") == "ac"
assert edit_str("abc##d######") == ""
assert edit_str("#######") == ""
assert edit_str("") == ""
