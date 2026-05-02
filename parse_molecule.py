import re
from logging import getLogger, ERROR, basicConfig


LOGGER = getLogger()
FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
basicConfig(level=ERROR, format=FORMAT)


def molecule_to_list(formula: str) -> list:
    return re.findall(r'[A-Z][a-z]*|\d+|[(){}\[\]]', formula)


def is_valid_brackets(formula: str) -> bool:
    if formula[0] in ')}]':
        return False

    brackets = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    in_formula = []
    for mark in formula:
        if mark in '({[':
            in_formula.append(mark)
        if mark in ')}]':
            if mark == brackets[in_formula[-1]]:
                in_formula.pop()
            else:
                return False

    if (len(in_formula)) > 0:
        return False

    return True


def get_count(molecule_list: list, index: int) -> int:
    count = 1
    if index + 1 < len(molecule_list):
        if molecule_list[index + 1].isdigit():
            count = int(molecule_list[index + 1])
    return count


def parse_molecule(formula: str) -> dict:
    if not is_valid_brackets(formula):
        LOGGER.error('The sequence of parentheses in the "%s" formula is broken', formula)
        return {}

    molecule_list = molecule_to_list(formula)
    atoms: list[dict[str, int]] = [{}]
    for index, mark in enumerate(molecule_list):
        if mark.isalpha():
            count = get_count(molecule_list, index)
            atoms[-1][mark] = atoms[-1].get(mark, 0) + count
        if mark in '({[':
            atoms.append({})
        if mark in ')}]':
            in_brackets = atoms.pop()
            mult = get_count(molecule_list, index)
            for element, count in in_brackets.items():
                atoms[-1][element] = atoms[-1].get(element, 0) + in_brackets.get(element, 1) * mult

    return atoms[0]


def check_parse_molecule(formula: str, expected_result: dict):
    result = parse_molecule(formula)
    try:
        assert result == expected_result
    except AssertionError:
        LOGGER.error("parse_molecule(%s) returned: %s, expected: %s",
                     formula, result, expected_result)


check_parse_molecule("H2O", {'H': 2, 'O': 1})
check_parse_molecule("Mg(OH)2", {'Mg': 1, 'O': 2, 'H': 2})
check_parse_molecule("K4[ON(SO3)2]2", {'K': 4, 'O': 14, 'N': 2, 'S': 4})
