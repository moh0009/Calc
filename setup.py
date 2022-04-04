from setuptools import setup,find_packages

calssifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Education",
    "Operating System :: Microsoft :: Windows",
    "License :: OSI Approved :: MIT License",
    "Programing Language :: Python :: 3"
]

setup(
    name = "calc",
    version = "1.0",
    description = "calculator",
    long_description = open("Readme.txt").read()+"\n\n"+open("changelog.txt").read(),
    url ="" ,
    author="moh0009",
    author_email = "23ii.mancy@gmail.com",
    license = "MIT",
    classifiers = calssifiers,
    keywords = "calculator",
    packages = find_packages(),
    install_requires = [""]
)
