from setuptools import setup

setup(
    name='am',
    version='0.1',
    py_modules=['am'],
    install_requires=[
        'Click',
    ],

    entry_points='''
        [console_scripts]
        am=am:cli
    '''
)