from pathlib import Path

import setuptools

requirements = Path("requirements.txt").read_text().splitlines()
readme = Path("README.md").read_text()
project_license = Path("LICENSE").read_text()

setuptools.setup(
    name="stream-cli",
    author="Redouane Elkaboussi",
    author_email="elkaboussi@pm.me",
    version=0.2,
    description="stream movies directly from your terminal!",
    long_description=readme,
    packages=requirements,
    license=project_license,
)
