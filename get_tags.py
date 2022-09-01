#! /usr/bin/python
""" begin

    Returns:
        _type_: _description_
"""


def get_tags(tfile):
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    with open(tfile, "r",
              encoding='utf-8') as tagfile:
        j = tagfile.read()
        return j.split(",")
