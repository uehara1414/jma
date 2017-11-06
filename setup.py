import os
from setuptools import setup


longDesc = ""
if os.path.exists("README.md"):
    longDesc = open("README.md").read().strip()

setup(
    name="jma",
    version="0.1.0",
    author="uehara1414",
    author_email="",
    description="get weather data from jma",
    long_description=longDesc,
    license="MIT License",
    keywords="python jma weather",
    url="https://github.com/uehara1414/jma",
    packages=['jma'],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
