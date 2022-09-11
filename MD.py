import YAML


class MD(YAML):
    def __init__(self, frontmatter, file):
        super().__init__(frontmatter, file)

    def get_frontmatter(self):
        return super().get_frontmatter()

    def get_file(self, file):
        return super().get_file()

    def __str__(self):
        return super().__str__()

    def _to_txt(self, file):
        return self.get_file(file)
