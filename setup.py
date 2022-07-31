'''
Created on 23-Feb-2016

@author: psi phi
'''
from setuptools import setup
setup(
    name='Online Book Store',
    version=1.0,
    url='https://github.com/phisyche/bookstore',
    author='psi phi',
    author_email='phisyche@gmail.com',
    description='A shopping cart',
    long_description=__doc__,
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    packages=['BookStore'],
    install_requires=[
        'virtualenv>=14.0.3',
        'Flask>=0.10.1',
        'flask-restful>=0.3.5',
        'pymysql>=0.7.1',
        'pymongo>=3.2.3',
        'jsonpickle>= 0.9.3'
    ]
      
)
