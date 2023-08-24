"""The setup script."""

from setuptools import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'matplotlib',
    'networkx',
    'numpy',
    'scikit_learn',
    'scipy',
    'stopit',
    'sympy',
    'torch',
    'tqdm'
]



setup(
    name='DAG_search',
    version=1.0,
    description = "An open source python library symbolic regression based on searching the space of DAGs.",
    long_description = readme,
    author="Paul Kahlmeyer",
    author_email='paul.kahlmeyer@uni-jena.de',
    url = 'https://github.com/kahlmeyer94/DAG_search',
    packages = ['DAG_search'],
    install_requires = requirements
)