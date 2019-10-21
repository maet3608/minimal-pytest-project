from setuptools import setup, find_packages

import mymath

setup(
    name='mymath',
    version=mymath.__version__,
    author='Author name',
    author_email='author@gmail.com',
    description='Example for a minimal Python project with pytest support',
    packages=find_packages(),
    install_requires=[],  # e.g. ['numpy >= 1.11.1', 'matplotlib >= 1.5.1']
)

