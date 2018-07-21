import setuptools


setuptools.setup(
    name="argconf",
    version="0.0.1",
    author="Ralph Tang",
    author_email="r33tang@uwaterloo.ca",
    description="Simple library for parsing hierarchical configurations.",
    url="https://github.com/daemon/argconf",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)