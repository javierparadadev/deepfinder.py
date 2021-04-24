from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='deepfinder',
    packages=find_packages(),
    version='0.0.1',
    description='',
    author='Javier Parada',
    author_email="javierparada@protonmail.com",
    license='MIT',
    url="https://github.com/parada3desu/deepfinder.py",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "deepfinder"},
    python_requires=">=3.6",
)
