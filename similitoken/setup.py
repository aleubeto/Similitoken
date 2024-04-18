from setuptools import setup, find_packages

setup(
    name="similitoken",
    author="Alejandro Ubeto",
    version="0.1",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "pythonparser @ https://github.com/m-labs/pythonparser/archive/master.zip",
        "matplotlib"
    ],
)
