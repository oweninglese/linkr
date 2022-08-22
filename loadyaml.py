#!/usr/bin/python
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

import os
import re


from linkr import (arts, load_folder, search_yaml)
from makesubs import (suball)


def load_folder():
    """ load all md in TESTDIR and append Post object to files dict list
Args:
    TESTDIR (folder): folder containing md files
Returns:
    list: [list of dicts] --> [filename]: [Post object]"""
    for filename in os.listdir(arts):
        if filename.endswith(".md"):
            tfi = arts + filename
            suball(tfi)
    return "Done"


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
