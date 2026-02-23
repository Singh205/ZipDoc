from setuptools import setup, find_packages

setup(
    name="zipdoc",
    version="1.0.0",
    packages=find_packages(),
    install_requires=["tqdm"],
    entry_points={
        "console_scripts": [
            "zipdoc=zipdoc.cli:main",
        ],
    },
    author="Akshaj Singh",
    description="ZipDoc - A CLI-based PDF compression tool",
)
