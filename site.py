#!/usr/bin/python
"""Web site tools for flask site hosting mkdocs."""


import sys
import os
from flask import Flask
from flask import url_for
from flask import redirect
import jinja2
import markdown
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import Config as C
from tester import BASEDIR
import frontmatter as fm


BASE = declarative_base()
app = Flask(__name__, static_folder='static', template_folder='templates')
base_dir = os.path.abspath(os.path.dirname(__file__))
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'),
                               autoescape=True)
app.debug = True

ARTSDIR = C['ARTDIR']
BASEDIR = C['BASEDIR']
ALPH = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
BUCKETS = [[i] for i in ALPH]
testfiles = [file for file in os.listdir(BASEDIR
                                         + ARTSDIR) if file.endswith(".md")]
PRETTY = list(ALPH)
NEWNAV = {}

for letter in PRETTY:
    if not NEWNAV.get(letter):
        NEWNAV[letter] = []
MDFILES = [file[:-3] for file
           in os.listdir(f'{BASEDIR}/docs/')
           if file.endswith(".md")]
HTMLFILES = [f'{file}.html' for file in MDFILES]

ENGINE = create_engine(f'sqlite:///{BASEDIR}/notes.db')
BASE.metadata.create_all(ENGINE)
DBSESSION = sessionmaker(bind=ENGINE)

TESTFILE = 'A Treaty Right To Education.md'


def add_to_db(note):
    """Add a note to the database."""
    session = DBSESSION()
    session.add(note)
    session.commit()
    session.close()


def make_note_from_file(filename):
    """
    Make a note from a file.

    @param filename - the file to make a note from
    @return the note
    """
    nfile = fm.load(filename)
    fmatter = nfile.metadata
    content = nfile.content
    return Note(title=fmatter['title'], content=content,
                source=fmatter['source'],
                tags=fmatter['tags'], created=fmatter['created'],
                link=fmatter['link'], author=fmatter['author'])


def buildnav(notes):
    """
    Build the navigation dictionary.

    This is a dictionary of buckets,
    each of which is a list of notes.
    @param notes - the notes dictionary
    @return the navigation dictionary
    """
    nav = []
    for i in notes:
        nav = nav + [i]
    nav.sort()
    navi = {}
    for i in BUCKETS:
        for j in nav:
            if j[0] == i[0]:
                if j[0] in navi:
                    navi[i[0]] += [j]
                else:
                    navi[i[0]] = [j]
    return navi


"""
NAVI = buildnav(testfiles)
for abc in PRETTY:
    for article in NAVI.values():
        for lead in article:
            if lead[0] == abc:
                NEWNAV[abc] += [lead]
for letter in NAVI:
    for article in NAVI[letter]:
        NEWNAV[letter] += [str([article[:-3] + '.html']).replace(' ', '_')] """


def render_temp(template, **params):
    """Render a template."""
    temp = jinja_env.get_template(template)
    return temp.render(params)


navig = buildnav(HTMLFILES)


@app.route('/site')
@app.route('/linkr')
@app.route('/index')
@app.route('/')
def index():
    """Website index.

    Returns:
        func: render_template -> index.html
    """
    localnavi = navig
    localnotes = testfiles
    return render_temp("index.html",
                       posts=localnotes,
                       nav=localnavi)


@app.route("/site/<filename>/index.html")
@app.route('/linkr/<filename>.html')
@app.route('/site/<filename>.html')
def single_file(filename):
    """Single file.

    Args:
        filename (str): filename

    Returns:
        func: render_template -> <singlefile>/index.html
    """
    fname = f'{filename}.html'
    return render_temp(f'/site/{fname}',
                       nav=navig)


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
              '/' + mdfile + '.html',
              'w', encoding="utf-8") as fuler:
        fuler.seek(0, 0)
        fuler.write("{% extends 'index.html' %}\n\t{% block file %}\n")
        fuler.write(html)
        fuler.seek(0, 2)
        fuler.write("\n\t{% endblock %}")
    return str(html)


class Note(BASE):
    """Create a note object."""

    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    content = Column(String(250), nullable=False)
    created = Column(String(250), nullable=False)
    updated = Column(String(250), nullable=False)
    link = Column(String(250), nullable=False)
    tags = Column(String(250), nullable=True)
    links = Column(String(250), nullable=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format."""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'link': self.link,
            'created': self.created,
        }

    @property
    def serialize_tags(self):
        """Return object data in easily serializeable foirmat."""
        return {
            'tags': self.tags,
        }

    @property
    def serialize_links(self):
        """Return object data in easily serializeable format."""
        return {
            'links': self.links,
        }


# html_fs = [md_to_html(file) for file in MDFILES]

# if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=5000, debug=True)
