"""Python setup.py for fastapi_backend package"""
from pathlib import Path
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("fastapi_backend", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with Path(__file__).parent.joinpath(*paths).open(
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="fastapi_backend",
    version=read("fastapi_backend", "VERSION"),
    description="Awesome fastapi_backend created by gparpinelli",
    url="https://github.com/gparpinelli/fastapi-backend/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="gparpinelli",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["fastapi_backend = fastapi_backend.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
