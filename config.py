#! /usr/bin/python
"""AI is creating summary for 
    """""" begin

    Returns:
        _type_: _description_
"""

import os
Config: dict = {}
Config.ARTDIR: str = '/vault/'
Config.TAGS: str = ''
Config.TFILE: str = 'linkr/TAGS.csv'
Config.BASEDIR: str = os.path.abspath(os.path.dirname(__file__))
Config.ARTS: str = Config.BASEDIR + Config.ARTDIR
