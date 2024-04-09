from setuptools import setup, find_packages

setup(
    name="similitoken",
    author="Alejandro Ubeto",
    version="0.1",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        'difflib',
    ],
    dependency_links=[
        'https://github.com/m-labs/pythonparser/tarball/master#egg=pythonparser-1.0',
    ],
)
