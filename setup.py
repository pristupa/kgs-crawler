from setuptools import setup


setup(
    name='kgs_crawler',
    version='0.1',
    python_requires='>=3.5',
    py_modules=['cli'],
    install_requires=[
        'Click==7.0',
        'sgfmill==1.1.1',
    ],
    entry_points='''
        [console_scripts]
        kgs_crawler=src.cli:cli
    ''',
)
