#! /usr/bin/python
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

import os
import re

import frontmatter as fm

from linkr import ARTDIR, get_tagfile, load_folder, resub, start
from linkr21 import check_tags

TAGS: str = ''
base_dir = os.path.abspath(os.path.dirname(__file__))
arts = base_dir + ARTDIR


load_folder()
start()
