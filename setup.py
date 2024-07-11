from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return a list of requirements 
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]#ensuring to replacce /n with a blank 
        if "-e ." in requirements :
            requirements.remove("-e .")


setup(

name = "end to end ml project",
version = '0.0.1',
author = 'Mr Raina',
author_email = 'a.raina4529@gmail.com',
packages = find_packages(),
install_requires =get_requirements('requirements.txt')


)