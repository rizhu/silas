import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="silas",
    version="0.0.1",
    author="Richard Hu",
    author_email="",
    description="linear algebra package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rhu2001/silas",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['silas=silas:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Unix"
    ],
    python_requires='>=3.6',
)