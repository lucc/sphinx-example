# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys, os
sys.path.insert(0, os.path.abspath('./.'))

project = 'bug-example'
copyright = '2022, me'
author = 'me'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    #'autoapi.extension',  # https://sphinx-autoapi.readthedocs.io/en/latest/
    #'sphinx.ext.autodoc',  # https://pypi.org/project/sphinx-autodoc-typehints/
    #'sphinx.ext.autosectionlabel',
    #'sphinx.ext.todo',
    'sphinx_argparse_cli',  # https://pypi.org/project/sphinx-argparse-cli/
    #'sphinx_autodoc_typehints',  # https://pypi.org/project/sphinx-autodoc-typehints/
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

man_pages = [ ('man', 'bug-example-1', 'bug example', '', 1) ]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
