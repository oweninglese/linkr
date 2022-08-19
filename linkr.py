#! /usr/bin/python
import json
import io
import os
import posixpath
import re
from datetime import date

import frontmatter as fm
import yamldown

artdir = '/vault/'
TAGS: str = ''
tfile = 'TAGS.csv'
base_dir = os.path.abspath(os.path.dirname(__file__))
arts = base_dir + artdir


def resub(tag, line):
    return re.sub(tag, f"[[{tag}]]", line)


def get_tagfile():
    with open(tfile, "r") as tagfile:
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


# print(i)

def sub_file(file, tag):
    """
    check single file for single tag
    """
    print(file, tag)
    with open(arts + file) as text:
        pst = text.readlines()
        yamlend = endof_yaml(pst)
        print(yamlend)
    with open(arts + file, 'w') as writer:
        for i, line in enumerate(pst):
            if i > int(yamlend):
                newline = resub(tag, line)
                writer.write(newline)
            else:
                writer.write(line)


def search_yaml(file, a):
    end = []
    for i, n in enumerate(file, 1):
        if i < 10: print(n)
        if a.search(n):
            print("found yaml")
            end = i

    return end


def endof_yaml(file):
    a = re.compile("---")
    b = []
    return search_yaml(file, a)


def tags_f(tag, pobject):
    sub_file(pobject['title'] + ".md", tag)


def check_tags(afile, tag):
    post = fm.load(arts + afile)
    if tag in post.content:
        post['tags'] += f" #{tag};"
        with open(arts + afile, 'w', encoding='utf-8') as text:
            text.write(fm.dumps(post))
        tags_f(tag, post)


load_folder()

for filename in os.listdir(arts):
    afile = str(filename) if filename.endswith(".md") else None
    with open(tfile, "r") as tagfile:
        j = tagfile.read()
        h = j.split(",")
        print(f"Checking : {afile} ")
        for i in h:
            check_tags(afile, i)



