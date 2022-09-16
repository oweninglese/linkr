#!/usr/bin/python

"""_summary_ of the module
    1) set up the config file GLOBALS
    2) print the config file GLOBALS
    3) Read the tags file and create a list of tags
    4) From List of tags create file per tag
    5) Read the articles folder and create a list of articles
    6) If article has tag, add article to tag file
    7) If article has tag, add tag to article file
    8) If article has tag, add tag to files tag list
"""
import os
import re
from datetime import date
import config as C
import frontmatter as fm
import tools as T

CONFIG = C.Config

ARTS = CONFIG['ARTS']
AUTHOR = CONFIG['AUTHOR']
ARTDIR = CONFIG['ARTDIR']
BASEDIR = CONFIG['BASEDIR']
CREATED = CONFIG['CREATED']
TAGSPATH = CONFIG['TAGSPATH']
TAGS = CONFIG['TAGS']
SOURCE = CONFIG['SOURCE']
TFILE = CONFIG['TFILE']


print(f"author : {AUTHOR}")
print(f"created : {CREATED}")
print(f"ARTS : {ARTS}")
print(f"ARTDIR : {ARTDIR}")
print(f"BASEDIR : {BASEDIR}")
print(f"TAGSPATH : {TAGSPATH}")

with open(TAGSPATH, 'r') as tagsfile:
    TAGS = tagsfile.read().splitlines()


def resub(tag: str, line: str) -> str:
    """
    Replace the tag with the line from the file.
    @param tag - the tag to replace with the line from the file.
    @param line - the line from the file.
    @returns the line with the tag replaced with the line from the file.
    """
    return re.sub(tag, f"[[{tag}]]", line)


ALLTAGS = [word for line in TAGS for word in line.split(',')]
cleartags = [tag.strip(" ") for tag in ALLTAGS]
cleartags = [tag.strip("") for tag in ALLTAGS]
while "" in cleartags:
    cleartags.remove("")
ALLTAGS = []


def fm_allfolder() -> None:
    """
    Load all md files in TESTDIR and append the author,
    source, tags, created, and title.
    @returns None
    """
    for file in os.listdir(ARTS):
        if file.endswith(".md"):
            post = fm.load(ARTS + file)
            post['author'] = AUTHOR
            post['source'] = SOURCE
            post['tags'] = ''
            post['created'] = CREATED
            post['title'] = file[:-3]
            with open(ARTS + file, 'w', encoding="utf-8") as text:
                text.write(fm.dumps(post))


# 1) create tag files from TAGS.csv
# T.create_tagfiles(cleartags)

# 2) tags frontmatter is not set until after next line
# fm_allfolder()

# 3) gather all files in ARTS directory
testfiles = [file for file in os.listdir(ARTS) if file.endswith(".md")]


def do_for_all_file_and_tags() -> None:
    """
    For each file in ARTS directory print the file name.

    Check for tags and write to tag files.
    @returns None
    """
    for file in testfiles:
        check_tags_and_write(file, cleartags)
    for testfile in testfiles:
        for tag in cleartags:
            with open(ARTS + testfile, 'r', encoding="utf-8") as reader:
                contents = reader.read()
                # 4) add tags to frontmatter
                T.add_tag(testfile, tag)
                # 5) add tags to tag files
                T.link_tags(testfile, tag)
                # 6) if tag in content make subs
                check_tags_and_write(tag, contents)

    def check_tags_and_write(tag, afile):
        """Check for tag and write to tag file."""
        if tag in afile:
            print(f'tag : {tag} in file : {testfile}')

            with open(ARTS + tag + ".md", 'a', encoding="utf-8") as text:
                text.write(f"[[{testfile}]]\n")
