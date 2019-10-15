""" Glouton setup.

"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    version="0.5.0",
    name="glouton",
    description="`Glouton is a cli program which helps you downloading satnogs data`",
    url="https://github.com/deckbsd/glouton-satnogs-data-downloader.git",
    license="MIT",
    author="deckbsd",
    install_requires=["requests"],
    python_requires='>=3',
    extras_require={"test": ["pytest"]},
    packages=find_packages(exclude=["tests", "docs"]),
    data_files=[('glouton', ['glouton/config.json'])],
    scripts=['bin/glouton'],
    keywords="satnogs, telemetry, satellite, payload, data, db, download",
    classifiers=[
        "Development Status :: 3 - Alpha", "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
)
