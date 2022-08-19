#! /usr/bin/python

""" begin


Keyword arguments:
argument -- description
Return: return_description
"""
import os

ARTDIR = '/final/'
TAGS: str = ''
TFILE = 'linkr/TAGS.csv'
base_dir = os.path.abspath(os.path.dirname(__file__))
arts = base_dir + ARTDIR


def link_article(tagfile, article):
    """link tag article to article with tag in it

    Args:
        tag (str): file name str to be filled
        article (str): mkdown file to be linked to tag"""
    tagfile.write(f"[[{article}]]")
    tagfile.write(f"#{article}")


def get_tags():
    """GET TAGS FROM TAGS.CSV
        Keyword arguments:
        argument -- description
        Return: return_description
    """
    with open(TFILE, "r", encoding='utf-8') as tagfile:
        j = tagfile.read()
        return j.split(",")


def check_file():
    """check if file exists
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return cleantags(get_tags())


def cleantags(tags):
    """ begin
    `
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    alltags = []

    for i in tags:
        pii = i.strip("#")
        opi = pii.strip(";")
        alltags.append(opi)
    return alltags


def get_articles():
    """get all articles in arts directory
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return [f for f in os.listdir(arts) if f.endswith(".md")]


ARTICLES = get_articles()
TAGS = check_file()


def start(tags, articles):
    """` begin
    ``a
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    for article in articles:
        cleartags = [tag.strip(" ") for tag in tags]
        while "" in cleartags:
            cleartags.remove("")
        for tag in cleartags:
            if tag in article:
                with open(arts + tag + ".md", "a", encoding='utf-8') as nfile:
                    nfile.write(f"\n[[{article}]]")
                    nfile.write(f"#{article}")
                    print(f"linked {article} to {tag}")


start(TAGS, ARTICLES)
