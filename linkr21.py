#! /usr/bin/python
import os
import re
from datetime import date
import frontmatter as fm
from linkr import ARTDIR, resub, tagfile, load_folder, start

TAGS: str = ''
base_dir = os.path.abspath(os.path.dirname(__file__))
arts = base_dir + ARTDIR


def check_tags(afile, tag):
    post = fm.load(arts + afile)
    if tag in post.content:
        post['tags'] += f" #{tag};"
        with open(arts + afile, 'w') as text:
            text.write(fm.dumps(post))


load_folder()
start()
