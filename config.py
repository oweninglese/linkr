#! /usr/bin/python
"""general config."""
from datetime import date
import os


Config = {
    'ARTS': os.path.join(os.path.dirname(__file__), 'vault/'),
    'AUTHOR': 'ohmanfoo',
    'ARTDIR': '/vault/',
    'CREATED': str(date.today()),
    'SOURCE': '#todo',
    'TAGSPATH': os.path.join(os.path.dirname(__file__), "TAGS.csv"),
    'BASEDIR': os.path.abspath(os.path.dirname(__file__)),
    'TAGS': '',
    'TFILE': os.path.join(os.path.dirname(__file__), "TAGS.csv"),
}
config = Config
