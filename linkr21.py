#! /usr/bin/python
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

import os

import frontmatter as fm

from linkr import ARTDIR, load_folder,\
    resub, start, tagfile, TAGS, base_dir

arts = base_dir + ARTDIR


def check_tags(afile, tag):
    post = fm.load(arts + afile)
    if tag in post.content:
        post['tags'] += f" #{tag};"
        with open(arts + afile, 'w', encoding="utf-8") as text:
            text.write(fm.dumps(post))


load_folder()
start()
