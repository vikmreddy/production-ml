from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

setup(
	name = 'mlproduction',
	packages = ['mlproduction'],
	version = 0.0.1,
	description = 'Machine Learning Production Application Framework',
	author = 'Vikram M. Reddy',
	author_email = 'vikram_reddy@berkeley.edu',
	url = 'https://github.com/vikmreddy/hindinlp.git'
	)