#! /usr/bin/python

""" begin


Keyword arguments:
argument -- description
Return: return_description
"""

import os

from linkr import TAGS, TFILE, base_dir, arts
from create_tagfiles import check_file, cleantags, get_tags

ARTDIR = '/final/'


def link_article(tagfile, article):
    """link tag article to article
    with tag in it

    Args:
        tag (str): file name str to fill
        article (str): mkdown file to link
    """
    tagfile.write(f"[[{article}]]")
    tagfile.write(f"#{article}")


def get_articles():
    """get all articles in arts directory
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return [f for f in os.listdir(arts)
            if f.endswith(".md")]


ARTICLES = get_articles()
CLTAGS = check_file()


def start(tags, articles):
    """` begin
    ``a
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    for article in articles:
        cleartags = [tag.strip(" ")
                     for tag in tags]
        while "" in cleartags:
            cleartags.remove("")
        for tag in cleartags:
            if tag in article:
                with open(arts + tag + ".md", "a",
                        encoding='utf-8') as nfile:
                    nfile.write(f"\n[[{article}]]")
                    nfile.write(f"#{article}")
                    print(f"linked {article}\
                          to {tag}")


start(CLTAGS, ARTICLES)
