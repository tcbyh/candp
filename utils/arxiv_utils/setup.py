from setuptools import setup, find_packages

setup(
    name='arxiv_utils',
    version='0.0.1',
    author='huxiaoyang',
    author_email='huxycn@qq.com',

    install_requires=[
        'fire',
        'loguru',
        'tqdm',
        'requests',
        'feedparser',
        'tabulate',
        'unidecode',
        'tenacity'
    ],

    entry_points={
      'console_scripts': [
          'arxiv_utils = arxiv_utils.main:main'
      ]
    },

    packages=find_packages(),

)