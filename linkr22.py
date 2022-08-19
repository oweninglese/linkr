#! /usr/bin/python
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

import json
import io
import os
import posixpath
import re
from datetime import date

import frontmatter as fm
import yamldown
from linkr import ARTDIR, TFILE

TAGS: str = ''
base_dir = os.path.abspath(os.path.dirname(__file__))
arts = base_dir + ARTDIR


def resub(tag, line):
    return re.sub(tag, f"[[{tag}]]", line)


def get_tagfile():
    with open(TFILE, "r") as tagfile:
        j = tagfile.read()
        return j.split(",")


def load_folder():
    """ load all md in TESTDIR and append Post object to files dict list
Args:
    TESTDIR (folder): folder containing md files
Returns:
    list: [list of dicts] --> [filename]: [Post object]"""
    for filename in os.listdir(arts):
        if filename.endswith(".md"):
            post = fm.load(arts + filename)
            post['author'] = 'ohmanfoo'
            post['source'] = '#todo'
            post['tags'] = ''
            post['created'] = str(date.today())
            post['title'] = filename[:-3]
            with open(arts + filename, 'w') as text:
                text.write(fm.dumps(post))


def check_tags(afile, tag):
    post = fm.load(arts + afile)
    if tag in post.content:
        # print("found tag " + tag)
        post['tags'] += f" #{tag};"
        with open(arts + afile, 'w') as text:
            text.write(fm.dumps(post))


load_folder()

for filename in os.listdir(arts):
    afile = str(filename) if filename.endswith(".md") else None
    with open(TFILE, "r") as tagfile:
        j = tagfile.read()
        h = j.split(",")
        print(f"Checking : {afile} ")
        for i in h:
            check_tags(afile, i)
