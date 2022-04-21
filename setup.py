from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in glass/__init__.py
from glass import __version__ as version

setup(
	name="glass",
	version=version,
	description="glass factory changes",
	author="Ahmed",
	author_email="ahmed.m@datasoft.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
