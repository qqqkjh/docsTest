# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'IdentityServer4'
author = 'Brock Allen & Dominick Baier'
copyright = '2020, Brock Allen & Dominick Baier'

version = '1.0.0'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

source_suffix = ['.rst']
master_doc = 'index'

language = 'en'  # 유효한 언어 코드

pygments_style = 'default'
highlight_language = 'csharp'

todo_include_todos = False

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'  # RTD 기본 테마
html_static_path = ['_static']   # 반드시 존재하도록 폴더 생성
html_favicon = 'favicon.ico'

# -- Options for other outputs (optional) -----------------------------------

htmlhelp_basename = 'IdentityServer4doc'

latex_elements = {}

latex_documents = [
    (master_doc, 'IdentityServer4.tex', 'IdentityServer4 Documentation',
     author, 'manual'),
]

man_pages = [
    (master_doc, 'identityserver4', 'IdentityServer4 Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'IdentityServer4', 'IdentityServer4 Documentation',
     author, 'IdentityServer4', 'One line description of project.',
     'Miscellaneous'),
]
