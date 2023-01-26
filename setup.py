# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='python-FWFile',
    version='0.0.1',
    author='OpusCode',
    author_email='contato@opssystem.com.br',
    url='https://www.opussystem.com.br',
    keywords=['fixed-width', 'fixed', 'width', 'text'],
    # packages=find_packages(exclude=['*tests*']),
    include_package_data=False,
    package_data={
    },
    install_requires=[
    ],
    license='MIT',
    description='Lib para gerar arquivos de texto (TXT) com tamanho fixado',
    long_description=open('README.md', 'r').read(),
    download_url='https://github.com/Defendi/python-FWFile',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms='any',
    tests_require=[
    ],
)
