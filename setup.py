from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    '''
    this function will return the list of requiremnets
    '''
    hypen_e_dot="-e ."
    requirement=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirement=[req.replace("\n","") for req in requirement]
    if hypen_e_dot in requirement:
        requirement.remove(hypen_e_dot)
    return requirement


setup(
name="End-to-End-Liver-Disease-prediction-and-monitoring-system",
version="0.0.1",
author="Ayushman",
author_email="humongous000001@gmail.com",
packages=find_packages(),
install_requires=get_requirements("requirements.txt")
)