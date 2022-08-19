#!/usr/bin/python
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

import os
import re

import frontmatter as fm
# import yamldown as yd

ARTDIR = '/vault/'
TAGS: str = ''
TFILE = 'linkr/TAGS.csv'
base_dir = os.path.abspath(os.path.dirname(__file__))
arts = base_dir + ARTDIR
TEST = """Aboriginal Peoples and Comprehensive Land Claims Negotiations
in Canada.md"""


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


def suball(tfi):
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    abc = checkforend(tfi)
    subs = 0
    tags = check_file(tfi)
    cleartags = [tag.strip(" ") for tag in tags]
    while "" in cleartags:
        cleartags.remove("")
    for tag in cleartags:
        with open(tfi, "r", encoding='utf-8') as file:
            text = file.readlines()
        with open(tfi, "w", encoding='utf-8') as source:
            for i, k in enumerate(text):
                if i < abc:
                    source.write(k)
                else:
                    line = resub(tag, k)
                    source.write(line)
                    subs += 1
    print(f"made {subs} substitions")


def resub(tag, line):
    """sumary_line"""
    return re.sub(tag, f"[[{tag}]]", line)


def checkforend(tfi):
    """sumary_line"""
    with open(tfi, "r", encoding='utf-8') as file:
        text = file.readlines()
        end = endof_yaml(text)

    return end


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


def check_file(tf):
    """sumary_line"""
    bad = get_tags(tf)
    return cleantags(bad)


def cleantags(tags):
    """sumary_line  remove empty tags"""
    alltags = []
    for i in tags.split():
        p = i.strip("#")
        o = p.strip(";")
        alltags.append(o)
    return alltags


def get_tags(post):
    """sumary_line"""
    afm = fm.load(post)
    return afm['tags']


def get_postcontent(tf):
    """sumary_line"""
    with open(tf, "r", encoding='utf-8') as post:
        return fm.load(post)


def get_post(tf):
    """sumary_line"""
    with open(tf, "r", encoding='utf-8') as post:
        return post


load_folder()
