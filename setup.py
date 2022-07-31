from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='diffReport',
    version=' 0.1.2',
    description='File comparison and report differences',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["diffReport", "fuzzyCompare", "markUp", "pdfParser"],
    install_requires=["fuzzywuzzy", "pandas", "pdfminer"],
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "Natural Language :: English",
        "Topic :: Text Processing :: Markup :: HTML"
    ],
    url="https://github.com/vish-nu-ram/diffReport",
    author="Vishnuram",
    author_email="vishnu.ram@hotmail.com",
)
