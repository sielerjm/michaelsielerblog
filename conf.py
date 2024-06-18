# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
#import sys
import ablog

#sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Michael Sieler'
copyright = '2024, Michael Sieler'
author = 'Michael Sieler'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'ablog',
    'sphinx.ext.intersphinx',
    # 'atom_absolute',
    'sphinxext.opengraph',
]

comments_config = {
   "hypothesis": True
}


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Michael Sieler's Blog"

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'ms-blog'
html_theme_path = ['_themes']

html_logo = 'media/logo/MS_Logo_Clr-WhBG-200px.png'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Favicon -----------------------------------------------------------------

html_favicon = 'favicon.ico'


# -- Blog -----------------------------------------------------------------

blog_title = "Michael Sieler's Blog"
blog_baseurl = 'https://blog.michaelsieler.com'
blog_path = 'archive'
fontawesome_link_cdn = 'https://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.min.css'

post_auto_excerpt = 2

blog_authors = {
    'Michael': ('Michael Sieler', 'http://michaelsieler.com'),
    # EXAMPLES for multiple authors
    # 'Anthony': ('Anthony Johnson', 'http://ohess.org'),
    # 'David': ('David Fischer', ''),
}

blog_default_author = 'Michael'

blog_locations = {
    'PDX': ('Portland, Oregon', ''),
    # Examples of multiple locations and websites
    # 'BND': ('Bend, Oregon', 'https://www.visitbend.com/'),
    # 'SAN': ('San Diego, CA', ''),
    # 'DHA': ('Dhaka, Bangladesh', 'https://wikitravel.org/en/Bangladesh'),
    # 'CUE': ('Cuenca, Ecuador', ''),
    # 'LKO': ('Lucknow, India', ''),
    # 'BCN': ('Barcelona, Spain', 'https://www.barcelona.cat/en/'),
    # 'MAD': ('Madrid, Spain', 'https://www.esmadrid.com/en'),
    # 'GEG': ('Spokane, Washington', ''),
}
blog_default_location = 'PDX'
blog_feed_archives = True
blog_feed_fulltext = True
blog_feed_length = 10


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
templates_path.append(os.path.join(
    '_themes', 'ms-blog'
))

templates_path.append(ablog.get_html_templates_path())

html4_writer = True

if os.environ.get('READTHEDOCS', None) == 'True':
    skip_pickling = True


# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# This will detect a blog post no matter where it is in /posts or what format
# https://ablog.readthedocs.io/manual/posting-and-listing/#posting-front-matter
blog_post_pattern = ["posts/*.rst", "posts/*.md"]


# Custom sidebar templates, maps document names to template names.
html_sidebars = {
   '**': [
          'postcard.html', 'recentposts.html',
          'tagcloud.html', 'categories.html',
          'archives.html', ]
}


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
