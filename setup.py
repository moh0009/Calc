from setuptools import setup,find_packages

calssifiers = [
    "Development Status :: 5 - Production/Stable",
    "Programming Language :: Python :: 3"

]

setup(
    name = "moh0009-calc",
    version = "1.0",
    description = "calculator",
    long_description = "Readme.md",
    url ="https://github.com/moh0009/Calc" ,
    author="moh0009",
    author_email = "23ii.mancy@gmail.com",
    license = "MIT",
    classifiers = calssifiers,
    keywords = ["calculator","calc"],
    packages = find_packages(),
    install_requires = [""]
)
