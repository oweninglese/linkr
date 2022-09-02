#! /usr/bin/python
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
import frontmatter as fm

from linkr import TFILE, arts, load_folder, start


def check_tags(afile, tag):
    post = fm.load(arts + afile)
    if tag in post.content:
        post['tags'] += f" #{tag};"
        with open(arts + afile, 'w', encoding="utf-8") as text:
            text.write(fm.dumps(post))
