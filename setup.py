'''
    Sphinxcontrib-lpblocks
    ~~~~~~~~~~~~~~~~~~~~~~

    Sphinx extension to support Literate Programming.
'''

import importlib
import io
import os
from setuptools import setup, find_packages

project = 'testing-lpblocks'
ns, pkg = project.split('-')
ABOUT = "%s.%s.__about__" % (ns, pkg)
VERSION = "%s.%s.__version__" % (ns, pkg)

about = importlib.import_module(ABOUT)
version = importlib.import_module(VERSION)

def readfile(filename):
    with io.open(filename, encoding="utf-8") as stream:
        return stream.read().split("\n")


readme = readfile("README.rst")

setup(
    name=project,
    version=version.VERSION,
    url=about.URL,
    download_url=about.PYPI,
    license=about.LICENSE,
    author=about.AUTHOR,
    author_email=about.EMAIL,
    description=about.SUMMARY,
    long_description="\n".join(readme),
    long_description_content_type='text/x-rst',
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['sphinx', 'sphinx-rtd-theme'],
    namespace_packages=[ns],
)
