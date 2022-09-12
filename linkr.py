#! /usr/bin/python
""" begin

    Returns:
        _type_: _description_
"""

import os
import re
from datetime import date
from frontYAML import YAML
from config import Config as C
import frontmatter as fm

ARTDIR = C.ARTDIR
TAGS = C.TAGS
TFILE = C.TFILE
BASEDIR = C.BASEDIR
ARTS = BASEDIR + ARTDIR


def resub(tag, line):
    """sumary_line fm.load(afile)['summary']"""
    return re.sub(tag, f"[[{tag}]]", line)


def preload_folder():
    """ load all md in TESTDIR and append
    Post object to files dict list
    Args:
    TESTDIR (folder): folder containing md files
    eturns:
    list: [list of dicts] -->
    [fname]: [Post object]"""
    for fname in os.listdir(ARTS):
        if fname.endswith(".md"):
            post = fm.load(ARTS + fname)
            post['author'] = 'ohmanfoo'
            post['source'] = '#todo'
            post['tags'] = ''
            post['created'] = str(date.today())
            post['title'] = fname[:-3]
            with open(ARTS + fname, 'w',
                      encoding="utf-8") as text:
                text.write(fm.dumps(post))


def sub_file(file, tag):
    """
    check single file for single tag
    """
    print(file, tag)
    with open(ARTS + file,
              encoding="utf-8") as text:
        pst = text.readlines()
        yamlend = endof_yaml(pst)
    with open(ARTS + file, 'w',
              encoding="utf-8") as writer:
        for i, line in enumerate(pst):
            if i > int(yamlend):
                newline = resub(tag, line)
                writer.write(newline)
            else:
                writer.write(line)


def tags_f(tag, pobject):
    """sumary_line fm.load(afile)['summary']"""
    sub_file(pobject['title'] + ".md", tag)


def check_tags_and_write(afile, tag):
    """sumary_line fm.load(afile)['summary']"""
    post = fm.load(ARTS + afile)
    if tag in post.content:
        post['tags'] += f"#{tag} "
        with open(ARTS + afile, 'w', encoding='utf-8') as text:
            text.write(fm.dumps(post))
        tags_f(tag, post)


def create_tagfiles():
    for fname in os.listdir(ARTS):
        next_file = str(fname) if fname.endswith(".md") else None
        with open(TFILE, "r", encoding="utf-8") as tagfile:
            all_tags = tagfile.read()
            tags_list = all_tags.split(",")
            for pick in tags_list:
                check_tags_and_write(next_file, pick)


def search_yaml(file, a):
    """
Find last str(a) lineno in file.
Used to find last line with symbol: '---'
"""
    end = []
    for i, nii in enumerate(file, 1):
        if a.search(nii):
            end = i
    return end


def endof_yaml(file: str):
    """
    Find end of frontmatter with symbol: ---
    Used to call search_yaml with correct regex
    """
    import re
    abc = re.compile("---")
    return search_yaml(file, abc)


def checkforend(file: str):
    """ Return end lineno of frontmatter section"""
    with open(file, "r", encoding='utf-8') as afile:
        text = afile.readlines()
        end = endof_yaml(text)
    return end
