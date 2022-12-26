from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules= cythonize("indexedPQ.pyx",compiler_directives={'language_level' : "3"}))
# setup(ext_modules= cythonize("indexedPQnoPy.pyx"))