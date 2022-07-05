from setuptools import setup

with open("README.md","r") as fh:
    long_description = fh.read()
setup(
    name='diffReport',
    version=' 0.0.3',
    description='File comparison and report differences',
    py_modules=["diffReport","fuzzyCompare","markUp","pdfParser"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/vish-nu-ram/diffReport",
    author="Vishnuram",
    author_email="vishnu.ram@hotmail.com"
)
