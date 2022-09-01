#! /usr/bin/python
""" begin

    Returns:
        _type_: _description_
"""

import os
import re
from datetime import date

import frontmatter as fm

ARTDIR = '/vault/'
TAGS: str = ''
TFILE = 'linkr/TAGS.csv'
base_dir = os.path.abspath(os.path.dirname(__file__))
arts = base_dir + ARTDIR


def resub(tag, line):
    """sumary_line fm.load(afile)['summary']"""
    return re.sub(tag, f"[[{tag}]]", line)


def get_tagfile():
    """sumary_line fm.load(afile)['summary']"""
    with open(TFILE, "r",
              encoding="utf-8") as gfile:
        jgf = gfile.read()
        return jgf.split(",")


def preload_folder():
    """ load all md in TESTDIR and append
    Post object to files dict list
    Args:
    TESTDIR (folder): folder containing md files
R   eturns:
    list: [list of dicts] -->
    [fname]: [Post object]"""
    for fname in os.listdir(arts):
        if fname.endswith(".md"):
            post = fm.load(arts + fname)
            post['author'] = 'ohmanfoo'
            post['source'] = '#todo'
            post['tags'] = ''
            post['created'] = str(date.today())
            post['title'] = fname[:-3]
            with open(arts + fname, 'w',
                      encoding="utf-8") as text:
                text.write(fm.dumps(post))


def sub_file(file, tag):
    """
    check single file for single tag
    """
    print(file, tag)
    with open(arts + file,
              encoding="utf-8") as text:
        pst = text.readlines()
        yamlend = endof_yaml(pst)
        print(yamlend)
    with open(arts + file, 'w',
              encoding="utf-8") as writer:
        for i, line in enumerate(pst):
            if i > int(yamlend):
                newline = resub(tag, line)
                writer.write(newline)
            else:
                writer.write(line)


def search_yaml(file, a):
    """sumary_line fm.load(afile)['summary']"""
    end = []
    for i, nic in enumerate(file, 1):
        if i < 10 and a.search(nic):
            end = i
    return end


def endof_yaml(file):
    """sumary_line fm.load(afile)['summary']"""
    abc = re.compile("---")
    return search_yaml(file, abc)


def tags_f(tag, pobject):
    """sumary_line fm.load(afile)['summary']"""
    sub_file(pobject['title'] + ".md", tag)


def check_tags(afile, tag):
    """sumary_line fm.load(afile)['summary']"""
    post = fm.load(arts + afile)
    if tag in post.content:
        post['tags'] += f" #{tag};"
        with open(arts + afile, 'w', encoding='utf-8') as text:
            text.write(fm.dumps(post))
        tags_f(tag, post)


def start():
    for fame in os.listdir(arts):
        allfile = str(fame) if fame.endswith(".md") else None
        with open(TFILE, "r", encoding="utf-8") as tagfile:
            j = tagfile.read()
            h = j.split(",")
            for ick in h:
                check_tags(allfile, ick)
