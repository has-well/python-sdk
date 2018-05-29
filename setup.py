from setuptools import find_packages, setup

from cloudipsp.configuration import __version__

with open('README.md', 'r') as f:
    readme = f.read()

requires_list = [
    'requests',
    'hashlib'
]

setup(
    name='cloudipsp',
    version=__version__,
    url='https://github.com/dimoncheg12/python-sdk/',
    license='MIT',
    description='SDK for cloudipsp clients.',
    long_description=readme,
    author='Dmitriy Miroshnikov',
    packages=find_packages(where='.', exclude=('tests*',)),
    install_requires=requires_list,
    classifiers=[
        'Environment :: Web Environment',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6'
    ])
