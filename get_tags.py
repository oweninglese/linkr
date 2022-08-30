#! /usr/bin/python
""" begin

    Returns:
        _type_: _description_
"""


def get_tags(tFILE):
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    with open(tFILE, "r",
              encoding='utf-8') as tagfile:
        j = tagfile.read()
        return j.split(",")
