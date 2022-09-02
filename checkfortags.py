#! /usr/bin/python
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

from config import Config as C
import frontmatter as fm

ARTDIR = C.ARTDIR
TAGS = C.TAGS
TFILE = C.TFILE
BASEDIR = C.BASEDIR
ARTS = BASEDIR + ARTDIR


def check_tags(afile, tag):
    post = fm.load(ARTS + afile)
    if tag in post.content:
        post['tags'] += f" #{tag};"
        with open(ARTS + afile, 'w', encoding="utf-8") as text:
            text.write(fm.dumps(post))
