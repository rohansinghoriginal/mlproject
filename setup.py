from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    requirements_list : List[str] = []
    return requirements_list

setup(
    name="my_project",
    version="0.1",
    author="Rohan",
    author_email="rohansingh13902@gmail.com",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "pymongo"
    ],
)