#! /usr/bin/python
""" classes for yaml and articles"""


class YAML:
    """ Frontmatter section functions """
    def __init__(self, frontmatter: str, file: str):
        self.frontmatter = frontmatter
        self.file = file

    def get_frontmatter(self):
        """get frontmatter section"""
        return self.frontmatter

    def get_filename(self):
        " Get filename from self.file "
        return self.file

    def __str__(self):
        return f"{self.frontmatter}"

    def search_yaml(self, file, a):
        """
        Find last str(a) lineno in file.
        Used to find last line with symbol: '---'
        """
        end = []
        for i, nii in enumerate(file, 1):
            if a.search(nii):
                end = i
        return end

    def endof_yaml(self, file: str):
        """
        Find end of frontmatter with symbol: ---
        Used to call search_yaml with correct regex
        """
        import re
        abc = re.compile("---")
        return self.search_yaml(file, abc)

    def checkforend(self, file: str):
        """ Return end lineno of frontmatter section"""
        with open(file, "r", encoding='utf-8') as afile:
            text = afile.readlines()
            end = self.endof_yaml(text)
        return end
