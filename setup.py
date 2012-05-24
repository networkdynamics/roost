#from distutils.core import setup
from setuptools import setup
from distutils.extension import Extension
import os.path
import sys

setup(
	name = 'roost',
	version = '0.1',
	#cmdclass = {'build_ext': build_ext},
	#ext_modules = ext_modules,
	packages = ['roost'],
	scripts = ['scripts/rtwtr'],
	
	# dependencies
	install_requires = ['oauth2>=1.5','pycurl>=7.18'],
	
	# project metadata
	author = 'Derek Ruths',
	author_email = 'druths@networkdynamics.org',
	description = 'Roost is a python-centric library for Twitter data collection and storage.',
	license = 'BSD',
	url = 'https://github.com/networkdynamics/roost',
	download_url = 'https://github.com/networkdynamics/roost'
)
