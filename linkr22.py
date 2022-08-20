#! /usr/bin/python
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

import json
import io
import os
import posixpath
import re
from datetime import date
from linkr import ARTDIR, resub, get_tagfile, load_folder, start
from linkr21 import check_tags
import frontmatter as fm
import yamldown

TAGS: str = ''
base_dir = os.path.abspath(os.path.dirname(__file__))
arts = base_dir + ARTDIR


load_folder()
start()
