from distutils.core import setup

setup(
    name = "Sebastian",
    version = "0.2",
    description = "A library for performing validations on chorales.",
    author = "Cal Peyser",
    packages = ['sebastian'],
    install_requires = ['music21==2.1.0']
)