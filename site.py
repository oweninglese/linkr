#!/usr/bin/python
"""Web site tools for flask site hosting mkdocs."""


import os
from flask import Flask
import jinja2
import markdown
from config import Config as C
from tester import BASEDIR

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


def render_temp(template, **params):
    """Render a template."""
    temp = jinja_env.get_template(template)
    return temp.render(params)


@app.route('/index')
@app.route('/')
def index():
    """Website index.

    Returns:
        func: render_template -> index.html
    """
    localnotes = testfiles
    navi = buildnav(testfiles)
    return render_temp("index.html",
                       posts=localnotes,
                       nav=navi)


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


print(buildnav(testfiles))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
