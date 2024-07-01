from setuptools import setup, find_packages
import codecs
import os
import platform

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Universal clear command definition.'
LONG_DESCRIPTION = 'A package that allows you to have a universal clear definition regardless of OS.'

# Setting up
setup(
    name="clear-command",
    version=VERSION,
    author="Malik Hassan",
    author_email="<malikkhabhassan@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    keywords=['python', 'command', 'clear', 'clear command', 'console clear', 'console'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)