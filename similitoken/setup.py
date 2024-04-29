from setuptools import setup, find_packages

setup(
    name="similitoken",
    version="0.1",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "pythonparser @ https://github.com/m-labs/pythonparser/archive/master.zip",
        "matplotlib",
    ],
    author=[
        "Alejandro Alfonso Ubeto Yañez",
        "Óscar Emiliano Ramírez Díaz",
        "Iker Guerrero González",
        "Ángel Rubén Vázquez Rivera",
        "Francisco Rocha Juárez",
    ],
    author_email=[
        "aleubeto.dev@gmail.com",
        "oscardiaz.dev@gmail.com",
        "ikerguerrero@yahoo.com",
        "developerrv1024@gmail.com",
        "rochapakito@gmail.com",
    ],
    license="MIT",
    url="https://github.com/aleubeto/Similitoken",
)
