from os import path

from setuptools import setup, find_packages, Extension
from codecs import open

readme_path = path.join(path.abspath(path.dirname(__file__)), 'README.rst')
with open(readme_path, encoding='utf-8') as readme:
    long_description = readme.read()

extensions = [
    Extension(
      'pyduktape2',
      ['pyduktape2.pyx']
    )
]

setup(
    name='pyduktape2',
    version='0.4.3',
    author='Stefano Dissegna',
    description='Python integration for the Duktape Javascript interpreter',
    long_description=long_description,
    url='https://github.com/phith0n/pyduktape2',
    license='GPL',
    keywords='javascript duktape embed',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3',
        'Programming Language :: JavaScript',
        'Topic :: Software Development :: Interpreters',
    ],
    packages=find_packages(exclude=['tests']),
    setup_requires=['setuptools>=18.0', 'Cython'],
    test_suite='tests',
    install_requires=['Cython'],
    ext_modules=extensions,
    include_package_data=True,
    zip_safe=False
)
