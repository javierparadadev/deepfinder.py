from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='deepfinder',
    version='0.0.6',
    description='Search attributes easily within structures of type dictionary, list and embedded substructures with '
                'simple format "dict.users.0.name".',
    author='Javier Parada',
    author_email='javierparada@protonmail.com',
    license='MIT',
    packages=['deepfinder'],
    url='https://github.com/parada3desu/deepfinder.py',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=">=3.6",
)
