from setuptools import setup

setup(
    name                = 'food2forkclient',
    version             = open('VERSION').read(),
    description         = 'Python package for Food2Fork API http://food2fork.com/api',
    long_description    = open('README').read(),
    author              = 'David Michael Brown',
    author_email        = 'davidmichaelbrown1@gmail.com',
    url                 = 'https://github.com/davidmichaelbrown/food2forkclient',
    packages            = ['food2forkclient', 'food2fork_tests'],
    #install_requires    = open( 'requirements.txt' ).read().split(),
    keywords            = 'food2fork recipes',
    license             = 'MIT',
    classifiers         = [
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: MIT'
    ]
)

