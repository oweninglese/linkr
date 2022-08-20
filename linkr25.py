#! /usr/bin/python
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

import os
from datetime import date
from linkr import TFILE

ARTDIR = '/final/'
TAGS: str = ''
base_dir = os.path.abspath(os.path.dirname(__file__))
arts = base_dir + ARTDIR


def get_tags():
    """`sumary_lin`e`
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    with open(TFILE, "r",
              encoding='utf-8') as tagfile:
        j = tagfile.read()
        return j.split(",")


def check_file():
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    bad = get_tags()
    return cleantags(bad)


def cleantags(tags):
    """sumary_line  remove empty tags"""
    alltags = []
    for i in tags:
        p = i.strip("#")
        o = p.strip(";")
        alltags.append(o)
    return alltags


TAGS = check_file()


def start(tags):
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    count = 0
    cleartags = [tag.strip(" ") for tag in tags]
    while "" in cleartags:
        cleartags.remove("")
    for tag in cleartags:
        with open(arts + tag + ".md", "w",
                  encoding='utf-8') as newfile:
            post = {'author': 'ohmanfoo',
                    'source': '#todo',
                    'tags': '',
                    'created': str(date.today())}
            post['title'] = tag
            newpost = ''.join(f"\n{str(i)}:
                        {post[i]}\n" for i in post)
            npi = f"---\n{newpost}\n---"
            newfile.write(npi)
            count += 1
            print(f"created newfile for {tag}")
    return f"created {count} files"


start(TAGS)
