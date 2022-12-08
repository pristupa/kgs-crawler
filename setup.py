from setuptools import setup


setup(
    name='kgs_crawler',
    version='0.1',
    python_requires='>=3.5',
    py_modules=['cli'],
    install_requires=[
        'certifi==2022.12.7',
        'chardet==3.0.4',
        'Click==7.0',
        'dataclasses==0.6',
        'idna==2.8',
        'kgs-crawler==0.1',
        'psycopg2-binary==2.7.7',
        'pydantic==0.20.1',
        'requests==2.21.0',
        'sgfmill==1.1.1',
        'urllib3==1.24.1',
        'ratelimit==2.2.1',
    ],
    entry_points='''
        [console_scripts]
        kgs_crawler=src.cli:cli
    ''',
)
