#!/usr/bin/python
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

import os
import re

from get_tags import get_tags
from makesubs import suball


def search_yaml(file, a):
    """sumary_line"""
    end = []
    # print(type(file))
    for i, nii in enumerate(file, 1):
        if a.search(nii):
            end = i
    return end


def endof_yaml(file):
    """sumary_line"""
    abc = re.compile("---")
    return search_yaml(file, abc)


load_folder()
