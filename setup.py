from setuptools import setup

with open("README.md", "r", encoding="utf-8") as file:
    LONG_DESCRIPTION = file.read()

setup(
    name="brightness",
    version="0.0.1",
    description="The effortless solution for managing screen brightness in Python.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/ekinpy/brightness",
    author="Ekin Aksu",
    license="MIT License",
    keywords="windows, screen, brightness",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11"
    ]
)
