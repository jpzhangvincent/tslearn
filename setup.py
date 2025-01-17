from setuptools import setup
from codecs import open
import numpy
import os
from Cython.Build import cythonize

# thanks Pipy for handling markdown now
ROOT = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(ROOT, 'README.md'), encoding="utf-8") as f:
    README = f.read()

# We can actually import a restricted version of tslearn that
# does not need the compiled code
import tslearn

VERSION = tslearn.__version__

setup(
    name="tslearn",
    description="A machine learning toolkit dedicated to time-series data",
    long_description=README,
    long_description_content_type='text/markdown',
    include_dirs=[numpy.get_include()],
    packages=['tslearn'],
    package_data={"tslearn": [".cached_datasets/Trace.npz"]},
    data_files=[("", ["LICENSE"])],
    install_requires=['numpy', 'scipy', 'scikit-learn', 'Cython', 'numba',
                      'joblib'],
    extras_require={'tests': ['pytest']},
    ext_modules=cythonize("tslearn/*.pyx", include_path=[numpy.get_include()]),
    version=VERSION,
    url="http://tslearn.readthedocs.io/",
    author="Romain Tavenard",
    author_email="romain.tavenard@univ-rennes2.fr"
)
