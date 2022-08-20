#! /usr/bin/python
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""

import os
import re

import frontmatter as fm

from linkr import (ARTDIR, TAGS, arts, base_dir, get_tagfile, load_folder,
                   resub, start)
from checkfortags import check_tags

load_folder()
start()
