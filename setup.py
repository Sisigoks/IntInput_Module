from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'This repository contains a Python function named `intinput` which prompts the user to input an integer value.'

# Setting up
setup(
    name="intinput",
    version=VERSION,
    author="Sibi Gokul",
    author_email="<Sisi.goks2008@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    keywords=['intinput'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)