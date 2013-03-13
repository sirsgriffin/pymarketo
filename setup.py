from setuptools import setup

setup(
    name='pymarketo',
    author='WebReply',
    author_email='',
    maintainer='Scott Griffin',
    maintainer_email='scott@loggly.net',
    version='0.1',
    packages=['marketo', 'tests'],
    long_description=open( 'README.rst' ).read(),
    install_requires=open( 'requirements.txt' ).read().split()
    )
