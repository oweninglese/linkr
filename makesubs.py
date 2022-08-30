#!/usr/bin/python
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
import frontmatter as fm

from linkr import arts, endof_yaml, resub

TEST = """Aboriginal Peoples and Comprehensive Land
Claims Negotiations in Canada.md"""
tfi = arts + TEST


def suball():
    """sumary_line"""
    abc = checkforend()
    subs = 0
    tags = check_file()
    cleartags = [tag.strip(" ") for tag in tags]
    while "" in cleartags:
        cleartags.remove("")
    for tag in cleartags:
        with open(tfi, "r", encoding='utf-8') as file:
            text = file.readlines()
        with open(tfi, "w", encoding='utf-8') as source:
            for i, k in enumerate(text):
                if i < abc:
                    source.write(k)
                else:
                    line = resub(tag, k)
                    source.write(line)
                    subs += 1
        print(f"made {subs} substitions")


def checkforend():
    """sumary_line"""
    with open(tfi, "r", encoding='utf-8') as file:
        text = file.readlines()
        end = endof_yaml(text)
    return end


def check_file():
    """check if file exists
    Keyword arguments:
    argument -- description
    Return: return_description
    """
    return cleantags(get_tags(tfi))


def cleantags(tags):
    """sumary_line  remove empty tags"""
    alltags = []
    for i in tags:
        p = i.strip("#")
        o = p.strip(";")
        alltags.append(o)
    return alltags


def get_tags(post):
    """sumary_line"""
    abc = fm.load(post)
    return abc['tags']


def get_postcontent(tfi):
    """sumary_line"""
    with open(tfi, "r", encoding='utf-8') as post:
        return fm.load(post)


def get_post(tfi):
    """sumary_line"""
    with open(tfi, "r", encoding='utf-8') as post:
        return post


bad = check_file()
cad = checkforend()
dad = suball()
print(dad)
