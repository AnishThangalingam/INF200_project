'''
Setup file for BioSim package.

To create a package, run python setup.py sdist in the directory containing
this file. To create a zip archive, run python setup.py sdist --formats=zip

The package will be placed in directory dist.

To install from the package, unpack it, move into the unpacked directory and
run

python setup.py install          # default location
python setup.py install --user   # per-user default location

See also
    http://docs.python.org/distutils
    http://docs.python.org/install
    http://guide.python-distribute.org/creation.html


This is taken from Hans Ekkehard Plesser, from his lecture
'''

__authors__ = "Anish Thangalingam & Majorann Thevarajah"
__email__ = 'anish.thangalingam@nmbu.no & majorann.thevarajah@nmbu.no'

from setuptools import setup

setup(name='BioSim',
      version='0.1',
      description='Modelling the Ecosystem of Rossumøya',
      author='Anish Thangalingam, NMBU & Majorann Thevarajah, NMBU',
      author_email='anish.thangalingam@nmbu.no & majorann.thevarajah@nmbu.no',
      requires=['numpy', 'matplotlib', 'pytest', 'pandas'],
      packages=['biosim'],
      scripts=['examples/save_fig_check.py'],
      )
