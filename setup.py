from setuptools import setup

setup(
    name = "Sebastian",
    version = "0.2",
    description = "A library for performing validations on chorales.",
    author = "Cal Peyser",
    packages = [
    	'sebastian.src',
    	'sebastian.src.Checks',
    	'sebastian.src.ChoraleAnalysis',
    	'sebastian.src.SebastianParser',
    	'sebastian.src.SebastianStructures',
    	'sebastian.src.Utils',
        'sebastian.tests',
        'sebastian.tests.IntegrationTests',
        'sebastian.tests.SebastianParserTests',
        'sebastian.tests.SebastianStructuresTests',
        'sebastian.tests.testfiles',
    ],
    package_data = {'sebastian.tests.testfiles': ["*.xml"]},
    install_requires = ['music21==2.1.0']
)
