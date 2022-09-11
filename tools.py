#!/usr/bin/python
"""_summary_
"""
import os
import re

import frontmatter as fm
from datetime import date
import config as C

ARTDIR = C.ARTDIR
TAGS = C.TAGS
TFILE = C.TFILE
BASEDIR = C.BASEDIR
ARTS = BASEDIR + ARTDIR


def checkforend(tfi):
    """ Return end for frontmatter section"""
    with open(tfi, "r", encoding='utf-8') as file:
        text = file.readlines()
        end = endof_yaml(text)
    return end


def cycle_check():
    for fname in os.listdir(ARTS):
        next_file = str(fname) if fname.endswith(".md") else None
        with open(TFILE, "r", encoding="utf-8") as tagfile:
            all_tags = tagfile.read()
            tags_list = all_tags.split(",")
            for pick in tags_list:
                check_tags_and_write(next_file, pick)


def clean_tags(tfi):
    """check if file exists
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return cleantags(get_tags(tfi))


def cleantags(tags):
    """sumary_line  remove empty tags"""
    alltags = []
    for i in tags:
        p = i.strip("#")
        o = p.strip(";")
        alltags.append(o)
    return alltags


def check_fortag(afile, tag):
    post = fm.load(ARTS + afile)
    if tag in post.content:
        post['tags'] += f" #{tag};"
        with open(ARTS + afile, 'w', encoding="utf-8") as text:
            text.write(fm.dumps(post))


def check_file(tfi):
    """check if file exists
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return cleantags(get_tags(tfi))


def check_tags_and_write(afile, tag):
    """sumary_line fm.load(afile)['summary']"""
    post = fm.load(ARTS + afile)
    if tag in post.content:
        post['tags'] += f"#{tag} "
        with open(ARTS + afile, 'w', encoding='utf-8') as text:
            text.write(fm.dumps(post))
        tags_f(tag, post)


def create_tagfiles(tags):
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
        with open(ARTS + tag + ".md", "w",
                  encoding='utf-8') as newfile:
            post = {'author': 'ohmanfoo',
                    'source': '#todo',
                    'tags': '',
                    'created': str(date.today())}
            post['title'] = tag
            newpost = ''.join(f"\n{str(i)}{post[i]}\n" for i in post)
            npi = f"---\n{newpost}\n---"
            newfile.write(npi)
            count += 1
            print(f"created newfile for {tag}")
    return f"created {count} files"


def endof_yaml(file):
    """sumary_line"""
    abc = re.compile("---")
    return search_yaml(file, abc)


def get_posttags(post):
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


def get_tags(tfile):
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    with open(tfile, "r",
              encoding='utf-8') as tagfile:
        j = tagfile.read()
        return j.split(",")


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


def link_arts(tags):
    """sumary_line
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    ARTDIR = '/final/'
    arts = BASEDIR + ARTDIR
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
            newpost = ''.join(f"\n{str(i)}{post[i]}\n" for i in post)
            npi = f"---\n{newpost}\n---"
            newfile.write(npi)
            count += 1
            print(f"created newfile for {tag}")
    return f"created {count} files"


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


def resub(tag, line):
    """sumary_line fm.load(afile)['summary']"""
    return re.sub(tag, f"[[{tag}]]", line)


def suball(tfi):
    """sumary_line"""
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


def search_yaml(file, a):
    """sumary_line"""
    end = []
    # print(type(file))
    for i, nii in enumerate(file, 1):
        if a.search(nii):
            end = i
    return end


def tags_f(tag, pobject):
    """sumary_line fm.load(afile)['summary']"""
    sub_file(pobject['title'] + ".md", tag)
