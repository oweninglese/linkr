#!/usr/bin/python
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

import os
import re


# import frontmatter as fm
# import yamldown as yd

ARTDIR = '/vault/'
TAGS: str = ''
TFILE = 'linkr/TAGS.csv'
base_dir = os.path.abspath(os.path.dirname(__file__))
arts = base_dir + ARTDIR
TEST = "Aboriginal Peoples and Comprehensive Land Claims Negotiations in Canada.md"
tfi = arts + TEST


def suball():
    """sumary_line"""
    abc = checkforend()
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


def checkforend():
    """sumary_line"""
    with open(tfi, "r", encoding='utf-8') as file:
        text = file.readlines()
        end = endof_yaml(text)
    return end


def search_yaml(file, abc):
    """sumary_line"""
    end = []
    for i, nbc in enumerate(file, 1):
        if abc.search(nbc):
            end = i
            print(f"end {end}")
    return end


def endof_yaml(file):
    """sumary_line"""
    abc = re.compile("---")
    return search_yaml(file, abc)


def check_file(tfi):
    """sumary_line"""
    bad = get_tags(tfi)
    return cleantags(bad)


def cleantags(tags):
    """sumary_line"""
    alltags = []
    for i in tags.split():
        poo = i.strip("#")
        oop = poo.strip(";")
        alltags.append(oop)
    return alltags


def get_tags(post):
    """sumary_line"""
    abc = fm.load(post)
    return abc['tags']


def get_postcontent(tfi):
    """sumary_line"""
    with open(tfi, "r", encoding='utf-8') as post:
        return fm.load(post)


def get_post(tfi):
    """sumary_line"""
    with open(tfi, "r", encoding='utf-8') as post:
        return post


bad = check_file(tfi)
cad = checkforend()
dad = suball()
print(dad)
