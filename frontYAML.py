#! /usr/bin/python
""" classes for yaml and articles"""


class front_yaml:

    """ Frontmatter section functions """
    def __init__(self, frontmatter: dict, file: str):
        self.frontmatter = frontmatter
        self.file = file

    def get_frontmatter(self):
        """get frontmatter section"""
        return self.frontmatter

    def get_title(self):
        " Get filename from self.file "
        return self.frontmatter['title']

    def get_author(self):
        """ get author from frontmatter """
        return self.frontmatter['author']

    def get_source(self):
        """ get source from frontmatter """
        return self.frontmatter['source']

    def get_tags(self):
        """ get tags from frontmatter """
        return self.frontmatter['tags']

    def get_created(self):
        """ get created from frontmatter """
        return self.frontmatter['created']

    def __str__(self):
        return f"{self.get_frontmatter()}"


class full_markdown(front_yaml):

    """ Full markdown file functions """
    def __init__(self, file: str):
        self.file = file
        self.frontmatter = self.get_frontmatter()
        self.content = self.get_content()
        self.title = self.get_title()
        self.author = self.get_author()
        self.source = self.get_source()
        self.tags = self.get_tags()
        self.created = self.get_created()

    def search_yaml(self, a):
        """
        Find last str(a) lineno in file.
        Used to find last line with symbol: '---'
        """
        with open(self.file, "r", encoding="utf-8") as text:
            print(text)
            last = []
            for i, line in enumerate(text):
                if a in line:
                    last = i
        return last[0]

    def endof_yaml(self):
        """ Return end lineno of frontmatter section
            Find end of frontmatter with symbol: ---
            Used to call search_yaml with correct regex
            """
        import re
        abc = re.compile("---")
        dabc = str(abc)
        return self.search_yaml(dabc)

    def checkforend(self):
        """ Return end lineno of frontmatter section"""
        return self.endof_yaml()

    def get_content(self):
        """ Get content from file """
        with open(self.file, "r", encoding='utf-8') as afile:
            text = afile.readlines()
            end = self.checkforend()
            content = text[end:]
        return content

    def get_frontmatter(self):
        """ Get frontmatter from file """
        with open(self.file, "r", encoding='utf-8') as afile:
            text = afile.readlines()
            end = self.checkforend()
            frontmatter = text[:end]
        return frontmatter


afile = 'A Treaty Right to Education.md'
front = {'author': 'ohmanfoo',
         'source': '#todo',
         'tags': '',
         'created': '2021-01-01',
         'title': afile}

frontmatter_section = front_yaml(front, afile)
print(frontmatter_section.get_frontmatter())
print(frontmatter_section.get_title())
print(frontmatter_section)

print(type(afile))
full_md = full_markdown(afile)
print(full_md)
