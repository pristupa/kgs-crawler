from setuptools import setup


setup(
    name='kgs_crawler',
    version='0.1',
    python_requires='>=3.5',
    py_modules=['cli'],
    install_requires=[
        'psycopg2-binary==2.7.7',
        'Click==7.0',
        'pydantic==0.20.1',
        'sgfmill==1.1.1',
    ],
    entry_points='''
        [console_scripts]
        kgs_crawler=src.cli:cli
    ''',
)
