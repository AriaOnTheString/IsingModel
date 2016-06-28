from distutils.core import setup
from Cython.Build import cythonize

setup(
  name = 'iterator',
  ext_modules = cythonize("iterator.py"),
)