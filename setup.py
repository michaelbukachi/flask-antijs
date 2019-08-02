"""
Flask-SQLite3
-------------

This is a flask extension the protects endpoints againts
'undefined' javascript values by checking the URL, query params and payloads.
"""
from setuptools import setup

version="0.0.1"

setup(
    name='Flask-AntiJs',
    version=version,
    url='https://github.com/michaelbukachi/flask-antijs',
    license='BSD',
    author='Michael Bukachi',
    author_email='michaelbukachi@gmail.com',
    description='An extension to check \'undefined\' values',
    long_description=__doc__,
    py_modules=['flask_antijs'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    setup_requires=['pytest-runner'],
    test_requires=['pytest', 'pytest-cov'],
    keywords='flask antijs',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
