
from distutils.core import setup
import sys, spgl

setup(name="Python SPGL",
	description="Python Client for the Stanford Portable Graphics Library",
	version="1.0",
	author="Alex Valderrama",
	author_email="avald@cs.stanford.edu",
	license="TODO",
	url="TODO",
	packages=['spgl'],
	package_data={'spgl': ['spl.jar']})