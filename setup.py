from setuptools import setup
from io import open

setup(
    name='almavik',
    version='3.9',
    description='Determination of the drop trajectory',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/markusLons/almavik',
    author='Markus.Alinas.Viktorias',
    author_email='v.tikhonova@g.nsu.ru',
    packages= ['almavik', 'almavik.exp1'],
    package_data={'almavik.exp1': ['*.jpeg']},
    #packages=find_packages(),
    #include_package_data=True,
    install_requires=[
        'opencv-python',
        'numpy',
        'PyQt5',
        'matplotlib',
    ]
)
