import sphinx_rtd_theme

project = 'DViki'
copyright = '2022, Megaman'
author = 'Megaman'

extensions = [
    'sphinx_rtd_theme',
]

templates_path = ['_templates']
exclude_patterns = []

html_logo = "logo.png"

html_theme = "sphinx_rtd_theme"

#html_theme = 'alabaster'
html_static_path = ['_static']
