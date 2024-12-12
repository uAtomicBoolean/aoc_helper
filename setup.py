import setuptools

with open("README.md", "r", encoding="utf-8") as file:
    LONG_DESCRIPTION = file.read()

VERSION = "0.1.0"
DESCRIPTION = "A python package to automate the repetivite tasks in the advent of code."

setuptools.setup(
    name="aoc_helper",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/uAtomicBoolean/aoc_helper",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=["requests"],
)
