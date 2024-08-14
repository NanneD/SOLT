# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SOLT'
copyright = '2024, Nanne A. Dieleman, Bernd Heidergott'
author = 'Nanne A. Dieleman, Bernd Heidergott'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_design",
	      "sphinx.ext.mathjax"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']

html_theme = "pydata_sphinx_theme"
html_show_sourcelink = False
html_show_copyright = False
html_favicon = "_static/SOLT_favicon.svg"
html_title = "SOLT"

html_theme_options = {
    "logo": {
        "alt_text": "SOLT - Home",
        "image_light": "_static/SOLT.svg",
        "image_dark": "_static/SOLT.svg",
    },
    "show_prev_next": False,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/NanneD/SOLT",
            "icon": "fa-brands fa-square-github",
            "type": "fontawesome",
        }
    ],
}

html_css_files = [
    "css/custom.css",
]
