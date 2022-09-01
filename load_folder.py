#! /usr/bin/python
""" begin

    Returns:
        _type_: _description_
"""
import os


def load_folder(arts):
    """ load all md in TESTDIR and append Post object to files dict list
Args:
    TESTDIR (folder): folder containing md files
Returns:
    list: [list of dicts] --> [filename]: [Post object]"""
    links = []
    for filename in os.listdir(arts):
        if filename.endswith(".md"):
            tfi = arts + filename
            links += tfi
#   suball(tfi)
    return links
