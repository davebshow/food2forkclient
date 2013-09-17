from setuptools import setup

execfile('yourpackage/version.py')

setup(
    name='food2forkclient',
    version =__version__,
    description='Python package for Food2Fork API http://food2fork.com/api',
    long_description=open('README.md').read(),
    author='David Michael Brown',
    author_email='davidmichaelbrown1@gmail.com',
    url='https://github.com/davidmichaelbrown/food2forkclient',
    packages=['food2forkclient', ],
    keywords='food2fork, recipes,',
    license='MIT',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: MIT'
    ]
)
