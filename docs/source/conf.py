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


# -- Project information -----------------------------------------------------

project = 'Dashboard-Prototype'
copyright = '2021, Norman Warthmann, Anibal Morales'
author = 'Norman Warthmann, Anibal Morales'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
   'sphinx.ext.doctest',
   'sphinx.ext.intersphinx',
   'sphinx.ext.todo',
   'sphinx.ext.coverage',
   'sphinx.ext.mathjax',
   'sphinx.ext.ifconfig',
   'sphinx.ext.viewcode',
   'sphinx.ext.githubpages'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
source_suffix = '.rst'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

import sphinx_rtd_theme

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'
html_add_permalinks = ''
master_doc = 'index'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# Configuration of Title Page
latex_maketitle = r'''
        \pagenumbering{Roman} %%% to avoid page 1 conflict with actual page
        \begin{titlepage}
            \vspace*{10mm} %%% * is used to give space from top, Title
            \flushright\textbf{\Huge {Creating a ReadtheDocs Documentation v1.0}}
            \vspace{0mm} %%% Sub-Title
            \textbf{\Large {A Step-by-Step Guide}}
            \vspace{50mm} % Author name
            \textbf{\Large {Anibal E. Morales}}
            \vspace{10mm} % Organization Name
            \textbf{\Large {Plant Breeding and Genetics Laboratory}}
            \vspace{0mm} % Division/Department
            \textbf{\Large {FAO/IAEA Joint Division}}
            \vspace{0mm} % City, Country
            \textbf{\Large {Seibersdorf, Austria}}
            \vspace{10mm} % Creation Date
            \normalsize Created: February, 2021
            \vspace*{0mm} % Last updated Date
            \normalsize  Last updated: 
            %% \vfill adds at the bottom a note or caution
            \vfill
            \small\flushleft {{\textbf {Please note:}} \textit {This is an important note at the bottom of the title page.}}
        \end{titlepage}
        \pagenumbering{arabic}
        \newcommand{\sectionbreak}{\clearpage}
'''
latex_elements = {
   'releasename': 'Version 1.2',
   'maketitle': latex_maketitle,
}
