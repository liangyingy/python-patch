import pathlib

from setuptools import setup, find_packages

import patch

setup(
    name="python-patch",
    version=patch.__version__,
    description="Library to parse and apply unified diffs.",
    long_description=(pathlib.Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    url=patch.__url__,
    author=patch.__author__,
    author_email="techtonik@gmail.com",
    license=patch.__license__,
    entry_points={"console_scripts": ["patch.py=patch:main"]},
    # packages=find_packages(exclude=["tests", "tests.*"]),
    packages = ["."],
    install_requires=[
    ],
    extras_require={
        # [all] pulls in all radio libraries
        "testing": [
            "pytest>=5.4.5",
        ],
    },
)