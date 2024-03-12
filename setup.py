# write a setup.py file to install the package

from setuptools import setup, find_packages

# read requirements from requirements.txt
with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='adni',
    version='0.1',
    packages=find_packages(),
    install_requires=required,
    entry_points={
        'console_scripts': [
            'adni=adni.__main__:main'
        ]
    }
)