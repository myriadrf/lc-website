# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sphinx_rtd_theme
import sphinx_git

# -- Project information -----------------------------------------------------

project = 'LibreCellular'
copyright = '2021-2022, LibreCellular contributors'
author = 'LibreCellular contributors'

# The full version, including alpha/beta/rc tags
release = '21.04'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    "sphinx.ext.autosectionlabel",
    "sphinx_rtd_theme",
    "sphinx_git"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['venv', '_build', 'Thumbs.db', '.DS_Store']

# This is where we place substitutions, such as for Unicode characters.
rst_epilog = """
.. include:: /substitutions.txt
"""

# Allow same section headings and thus labels to be used across documents.
autosectionlabel_prefix_document = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_theme = "sphinx_rtd_theme"

html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4
}

html_logo = 'images/LC_logo_200w.png'
html_favicon = 'images/LC_favicon_34x33.png'

html_show_sphinx = False

root_doc = 'index'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = ['lc-custom.css']

html_last_updated_fmt = '%b %d, %Y'

html_context = {
    'display_github': True,
    'github_user': 'myriadrf',
    'github_repo': 'lc-website',
    'github_version': 'master/' 
}
