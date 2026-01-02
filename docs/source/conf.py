import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

# Extensiones necesarias para autodoc
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

project = 'rps0'
copyright = '2025, Alejandro Cancelas Chapela'
author = 'Alejandro Cancelas Chapela'

# Documento principal
master_doc = 'index'

# Paths
templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# HTML
html_theme = 'alabaster'
html_static_path = ['_static']