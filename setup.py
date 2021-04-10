from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='deepgetter',
    packages=find_packages(),
    version='0.0.0',
    description='',
    author='Javier Parada',
    author_email="javierparada@protonmail.com",
    license='MIT',
    url="https://github.com/parada3desu/deepgetter.py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "deepgetter"},
    python_requires=">=3.6",
)
