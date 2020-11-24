import codecs
import posixpath
import re
import sys
import warnings
from hashlib import md5
from os import path

import docutils
from docutils import nodes
from docutils.core import Publisher
from docutils.frontend import OptionParser
from docutils.io import DocTreeInput, StringOutput
from docutils.readers.doctree import Reader as DoctreeReader
from docutils.utils import relative_path, new_document
from six import iteritems, text_type, string_types
from six.moves import cPickle as pickle

from sphinx import package_dir, __display_version__
from sphinx.application import ENV_PICKLE_FILENAME
from sphinx.builders import Builder
from sphinx.builders.html import StandaloneHTMLBuilder
from sphinx.config import string_classes
from sphinx.deprecation import RemovedInSphinx20Warning
from sphinx.environment.adapters.asset import ImageAdapter
from sphinx.environment.adapters.indexentries import IndexEntries
from sphinx.environment.adapters.toctree import TocTree
from sphinx.highlighting import PygmentsBridge
from sphinx.locale import _, l_
from sphinx.search import js_index
from sphinx.theming import HTMLThemeFactory
from sphinx.util import jsonimpl, logging, status_iterator
from sphinx.util.console import bold, darkgreen  # type: ignore
from sphinx.util.docutils import is_html5_writer_available
from sphinx.util.fileutil import copy_asset
from sphinx.util.i18n import format_date
from sphinx.util.inventory import InventoryFile
from sphinx.util.matching import patmatch, Matcher, DOTFILES
from sphinx.util.nodes import inline_all_toctrees
from sphinx.util.osutil import SEP, os_path, relative_uri, ensuredir, \
    movefile, copyfile
from sphinx.writers.html import HTMLWriter, HTMLTranslator

logger = logging.getLogger(__name__)


class CustomBuilder(StandaloneHTMLBuilder):

    name = 'custombuilder'

    def get_doc_context(self, docname, body, metatags):
        # type: (unicode, unicode, Dict) -> Dict[unicode, Any]
        """Collect items for the template context of a page."""
        # find out relations
        print("metatags", metatags)

        prev = next = None
        parents = []
        rellinks = self.globalcontext['rellinks'][:]
        related = self.relations.get(docname)
        titles = self.env.titles
        if related and related[2]:
            try:
                next = {
                    'link': self.get_relative_uri(docname, related[2]),
                    'title': self.render_partial(titles[related[2]])['title']
                }
                rellinks.append((related[2], next['title'], 'N', _('next')))
            except KeyError:
                next = None
        if related and related[1]:
            try:
                prev = {
                    'link': self.get_relative_uri(docname, related[1]),
                    'title': self.render_partial(titles[related[1]])['title']
                }
                rellinks.append((related[1], prev['title'], 'P', _('previous')))
            except KeyError:
                # the relation is (somehow) not in the TOC tree, handle
                # that gracefully
                prev = None
        while related and related[0]:
            try:
                parents.append({
                    'link': self.get_relative_uri(docname, related[0]),
                    'title': self.render_partial(titles[related[0]])['title']
                })
            except KeyError:
                pass
            related = self.relations.get(related[0])
        if parents:
            # remove link to the master file; we have a generic
            # "back to index" link already
            parents.pop()
        parents.reverse()

        # title rendered as HTML
        title = self.env.longtitles.get(docname)
        title = title and self.render_partial(title)['title'] or ''

        # Suffix for the document
        source_suffix = path.splitext(self.env.doc2path(docname))[1]

        # the name for the copied source
        if self.config.html_copy_source:
            sourcename = docname + source_suffix
            if source_suffix != self.config.html_sourcelink_suffix:
                sourcename += self.config.html_sourcelink_suffix
        else:
            sourcename = ''

        # metadata for the document
        meta = self.env.metadata.get(docname)

        # local TOC and global TOC tree

        nav_subchapter = """<li><a href="/{subchapter}.html">{subchapter_name}</a></li>"""

        nav_template = """
        <li class="menu-toggle-open">
            <a class="deep0" href="/{chapter}.html">
                <div class="al deep0-number">{chapter_number}</div>
                <div class="ar deep0-title">{chapter_name}</div>
            </a>
        </li>
        """

        nav_template_subitems = """
        <li class="menu-toggle-open">
            <a class="deep0" href="#">
                <div class="al deep0-number">{chapter_number}</div>
                <div class="ar deep0-title">{chapter_name}</div>
            </a>
            <ul class="deep1">
                {subchapters}
            </ul>
        </li>
        """

        result = ""
        for i, chapter in enumerate(self.env.toctree_includes['index']):
            if chapter in self.env.toctree_includes:
                chapter_items = self.env.toctree_includes[chapter]
                tmp = ""
                for item in chapter_items:
                    tmp += nav_subchapter.format(subchapter=item, subchapter_name=self.env.titles[item].children[0])
                result += nav_template_subitems.format(chapter_number=i+1, chapter_name=self.env.titles[chapter].children[0], subchapters=tmp)
            else:
                result += nav_template.format(chapter=chapter, chapter_number=i+1, chapter_name=self.env.titles[chapter].children[0])

        self_toc = TocTree(self.env).get_toc_for(docname, self)

        toc = self.render_partial(self_toc)['fragment']

        return dict(
            parents = parents,
            prev = prev,
            next = next,
            title = title,
            meta = meta,
            body = body,
            metatags = metatags,
            rellinks = rellinks,
            sourcename = sourcename,
            toc = toc,
            nav = result,
            # only display a TOC if there's more than one item to show
            display_toc = (self.env.toc_num_entries[docname] > 1),
            page_source_suffix = source_suffix,
        )


def setup(app):
    app.add_builder(CustomBuilder)