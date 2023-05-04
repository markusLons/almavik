from setuptools import setup, find_packages

setup(
    name='almavik',
    version='0.1.2',
    description='Determination of the drop trajectory',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/markusLons/almavik',
    author='Markus.Alinas.Viktorias',
    author_email='v.tikhonova@g.nsu.ru',
    packages=find_packages(),
    install_requires=[
        'opencv-python',
        'numpy',
        'PyQt5',
        'matplotlib',
    ],
    include_package_data=True,
)
