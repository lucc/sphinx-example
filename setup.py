from setuptools import setup

setup(
    name='bug-example',
    author='me',
    license='GPL',
    extras_require={'doc': [
        'sphinx',
        'sphinx-argparse-cli',
    ]},
    packages=['example'],
    entry_points={'console_scripts': ['bug-example = example.prog']}
)
