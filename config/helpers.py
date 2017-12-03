from typing import List

import os


def array_indented(level: int, l: List[str], quote_char='\'', comma_after=False) -> str:
    """
    return an array indented according to indent level
    :param level:
    :param l:
    :param quote_char:
    :param comma_after:
    :return:
    """
    out = "[\n"
    for x in l:
        out += (((level+1) * 4) * " ") + '{}{}{}'.format(quote_char, x, quote_char) + ",\n"
    out += ((level * 4) * " ") + "]"
    if comma_after:
        out += ","
    return out


def find_packages(path: str) -> List[str]:
    """
    A better version of find_packages than what setuptools offers
    This function needs to be deterministic.
    :param path:
    :return:
    """
    ret = []
    for root, _dir, files in os.walk(path):
        if '__init__.py' in files:
            ret.append(root.replace("/", "."))
    return sorted(ret)
