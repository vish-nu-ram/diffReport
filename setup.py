from setuptools import setup

with open("README.md","r") as fh:
    long_description = fh.read()
setup(
    name='diffReport',
    version=' 0.0.7',
    description='File comparison and report differences',
    long_description= long_description,
    long_description_content_type = "text/markdown",
    py_modules=["diffReport", "fuzzyCompare", "markUp", "pdfParser"],
    install_requires=["fuzzywuzzy", "pandas", "pdfminer", "python-Levenshtein"],
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
    author_email="vishnu.ram@hotmail.com",
)
