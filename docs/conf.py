 
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

 templates_path = ['_templates']

 

source_suffix = ['.rst']

 
master_doc = 'index'

# General information about the project.
project = 'IdentityServer4'
copyright = '2020, Brock Allen & Dominick Baier'
author = 'Brock Allen & Dominick Baier'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0.0'
# The full version, including alpha/beta/rc tags.
release = '1.0.0'
 
language = None

 
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

 
pygments_style = 'default'
highlight_language = 'csharp'

 
todo_include_todos = False


 
import os
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

 
html_favicon = 'favicon.ico'
 
html_static_path = ['_static']

 
htmlhelp_basename = 'IdentityServer4doc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
  
}
 
latex_documents = [
    (master_doc, 'IdentityServer4.tex', 'IdentityServer4 Documentation',
     'Brock Allen, Dominick Baier', 'manual'),
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

 