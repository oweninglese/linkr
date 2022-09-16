#! /usr/bin/python
"""begin.

Returns:
_type_: _description_
"""

import os
import re
from datetime import date
from typing import Pattern
from .config import Config as C
import frontmatter as fm  # type: ignore

ARTS = C['ARTS']
TFILE = C['TFILE']


def preload_folder() -> None:
    """
    Load all md files in TESTDIR and append Post object to files dict list.

    @returns:

        list: [list of dicts] -->
        [fname]: [Post object]
    """
    for fname in os.listdir(ARTS):
        if fname.endswith(".md"):
            post = fm.load(ARTS + fname)
            post['author'] = 'ohmanfoo'
            post['source'] = '#todo'
            post['tags'] = ''
            post['created'] = str(date.today())
            post['title'] = fname[:-3]
            with open(ARTS + fname, 'w',
                      encoding="utf-8") as text:
                text.write(fm.dumps(post))


def resub(tag: str, line: str) -> str:
    """
    Replace the tag with the line from the file.

    @param tag - the tag to replace with the line from the file.
    @param line - the line from the file.
    @returns the line with the tag replaced with the line from the file.
    """
    return re.sub(tag, f"[[{tag}]]", line)


def sub_file(file: str, tag: str) -> None:
    """
    Check single file for single tag.

    @param file - the file to check for the tag
    @param tag - the tag to check for
    """
    with open(ARTS + file,
              encoding="utf-8") as text:
        pst = text.read()
        yamlend = checkforend(pst)
    with open(ARTS + file, 'w',
              encoding="utf-8") as writer:
        for i, line in enumerate(pst):
            if i > int(yamlend):
                newline = resub(tag, line)
                writer.write(newline)
            else:
                writer.write(line)


def tags_f(tag: str, pobject: dict) -> None:
    """
    Given a tag and a pobject create a markdown file with the tag.
    as the title and the pobject's summary as the body.
    @param tag - the tag we are adding to the markdown file.
    @param pobject - the pobject we are adding to the markdown file.
    """
    sub_file(pobject['title'] + ".md", tag)


def check_tags_and_write(afile: str, tag: str) -> None:
    """
    Check if the tag is in the post. If it is, add the tag to the post's tags.
    @param afile - the file name of the post.
    @param tag - the tag we are checking for.
    """
    post = fm.load(ARTS + afile)
    if tag in post.content:
        post['tags'] += f"#{tag} "
        with open(ARTS + afile, 'w', encoding='utf-8') as text:
            text.write(fm.dumps(post))
        tags_f(tag, post)


def create_tagfiles() -> None:
    """
    Create a tagfile for each file in the directory.
    """
    for fname in os.listdir(ARTS):
        next_file = str(fname) if fname.endswith(".md") else None
        with open(TFILE, "r", encoding="utf-8") as tagfile:
            all_tags = tagfile.read()
            tags_list = all_tags.split(",")
            for pick in tags_list:
                check_tags_and_write(next_file, pick)


def search_yaml(file: list[str], a: Pattern[str]) -> list:
    """
    Find last str(a) lineno in file.
    Used to find last line with symbol: '---'
    """
    end: list = []
    end.extend(i for i, line in enumerate(file) if a.search(line))
    return end


def endof_yaml(file: list[str]) -> list:
    """
    Find end of frontmatter with symbol: ---
    Used to call search_yaml with correct regex
    """
    abc: Pattern[str] = re.compile("---")
    return search_yaml(file, abc)


def checkforend(file: str) -> str:
    """
    Return the end line number of the frontmatter section of a markdown file.
    @param file - the file to be checked.
    @return the end line number of the frontmatter section of a markdown file.
    Return end lineno of frontmatter section
    """
    with open(file, "r", encoding='utf-8') as afile:
        text: list[str] = afile.readlines()
        end = endof_yaml(text)
    return str(end[1])
