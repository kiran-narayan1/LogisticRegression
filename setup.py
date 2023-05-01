from setuptools import setup, find_packages
from typing import List



HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    try:

        requirements = []
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.replace('\n') for req in requirements ]

            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)

        return requirements


    except Exception as e:
        print(f'error found while installing packages: {e}')

setup(
    name='logistic regression',
    version='0.0.1',
    author='kiran narayan',
    author_email='@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages = find_packages()
  
)