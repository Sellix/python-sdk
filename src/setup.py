from setuptools import setup, find_packages

setup(
    name="sellix-python-sdk",
    version="1.0.1",
    packages=find_packages(),
    url='https://github.com/Sellix/python-sdk',
    install_requires=[
        'requests',
    ],
)