#!/usr/bin/python
""" classes for yaml and articles"""


class YAML:
    def __init__(self, frontmatter, file):
        self.frontmatter = frontmatter
        self.file = file

    def get_frontmatter(self):
        return self.frontmatter

    def get_file(self):
        return self.file

    def __str__(self):
        return f"frontmatter: {self.frontmatter} , file: {self.file}"
