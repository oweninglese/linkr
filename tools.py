#!/usr/bin/python
"""tools.py - tools for tags and links.

Returns:
_type_: None
"""
import os
import re
from datetime import date
from typing import Any, Match, Pattern

import frontmatter as fm
import markdown

from config import Config as C

ARTS = C['ARTS']
TFILE = C['TFILE']
BASEDIR = C['BASEDIR']


def checkforend(testfile: str) -> Match[str]:
    """
    Check the end of the yaml file for the end of the training session.

    @param tfi - the yaml file to check for the end of the training session.
    @returns the end of the yaml file.
    """

    def endof_yaml(file: list[str]) -> Any:
        """
        Given a file, return the end of the yaml frontmatter.

        Args:
                file (str): full file contents
        Returns:
            func: return position of end of yaml frontmatter
        """
        abc: Pattern = re.compile("---")
        return search_yaml(file, abc)

    def search_yaml(file: list[str], anyre: Pattern) -> list[int]:
        """
        Search the markdown file for the end of the frontmatter.

        Return the index of the end of the file.
        @param file - the yaml file to search for the end of the file.
        @param a - the pattern to search for in the file.
        @return the index of the end of the file.
        """
        end: list = []
        for i, nii in enumerate(file, 1):
            if anyre.search(nii):
                end = i
        return end

    with open(testfile, "r", encoding='utf-8') as file:
        text = file.readlines()
        end: Match[str] = endof_yaml(text)
    return end


def md_to_html(mdfile: str) -> str:
    """
    Take a markdown file and convert it to html.

    @param md - the markdown file to convert to html
    @returns the html file
    """
    with open(os.path.abspath('docs') +
              '/' + mdfile + '.md',
              'r', encoding="utf-8") as filer:
        text = filer.read()
        html = markdown.markdown(text)
    with open(os.path.abspath('static') +
              '/' + mdfile +
              '/index.html',
              'w', encoding="utf-8") as fuler:
        fuler.write(html)
    return str(html)


def link_tags(file: str, tag: str) -> None:
    """
    Given a file and a tag, link the tag to the file.

    @param file - the file to link to
    @param tag - the tag to link to the file
    """

    def add_tag(afile: str, tag: str) -> None:
        """
        Check if the tag is in the post.

        If it is, add the tag to the post's tags.
        Also, write the post to the file.

        @param afile - the file to write to
        @param tag - the tag to check for
        """
        post = fm.load(ARTS + afile)
        if tag in post.content:
            post['tags'] += f"#{tag} "
            with open(ARTS + afile, 'w', encoding='utf-8') as text:
                text.write(fm.dumps(post))

    def resub(tag: str, line: str) -> str:
        """Return line with string substitution made adding brackets.

        Args:
            tag (str): tag to be replaced
            line (str): line to be searched

        Returns:
            str: line with tag replaced
        """
        return re.sub(tag, f"[[{tag}]]", line)

    def enum_and_sub(testfile, abc, tag):
        """
        Enumerate the source file and replace the lines with the new tag.

        @param testfile - the file to enumerate and replace lines in.
        @param abc - the number of lines to skip.
        @param subs - the number of lines to replace.
        @param tag - the tag to replace with.
        """
        with open(ARTS + testfile, "r", encoding='utf-8') as file:
            text = file.readlines()
        with open(ARTS + testfile, "w", encoding='utf-8') as source:
            for i, k in enumerate(text):
                if i < abc:
                    source.write(k)
                else:
                    line = resub(tag, k)
                    source.write(line)
    enum_and_sub(file, checkforend(ARTS + file), tag)


def create_tagfiles(tags: list) -> str:
    """
    Create a new file for each tag in the tags list.

    @param tags - the tags list
    @returns the number of files created
    """
    count = 0
    cleartags = [tag.strip(" ") for tag in tags]
    while "" in cleartags:
        cleartags.remove("")
    for tag in cleartags:
        with open(ARTS + tag + ".md", "w",
                  encoding='utf-8') as newfile:
            post = {'author': 'ohmanfoo',
                    'source': '#todo',
                    'tags': '',
                    'created': str(date.today())}
            post['title'] = f"{tag}.md"
            newpost = ''.join(
                f"\n{str(i)} : {post[i]}\n" for i in post)
            npi = f"---\n{newpost}\n---"
            newfile.write(npi)
            count += 1
            print(f"created newfile for {tag}")
            return f"created {count} files"
