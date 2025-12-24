from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements


setup(
    name="ml_project_1",
    version="0.0.1",
    author="Naman",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
