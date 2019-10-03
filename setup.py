import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "silas",
    version = "0.0.5.6",
    author = "Richard Hu",
    author_email = "r.hu@berkeley.edu",
    description = "Linear algebra software running in terminal",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/rhu2001/silas",
    packages = setuptools.find_packages(),
    entry_points = {
        'console_scripts': ['silas=silas.silas_cli:main'],
    },
    classifiers = [
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: MacOS :: MacOS X",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Education",
        "Environment :: Console",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Operating System :: Unix"
    ],
    python_requires = '>=3.6',
)