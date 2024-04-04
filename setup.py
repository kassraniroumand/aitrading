from setuptools import find_packages
from setuptools import setup

with open("requirements_old.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='aitrading',
      version="0.0.7",
      description="aitrading appliucation",
      license="MIT",
      author="ai_trading team",
      author_email="fake@email.com",
      #url="https://github.com/lewagon/taxi-fare",
      install_requires=requirements,
      packages=find_packages(),
      test_suite="tests",
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      zip_safe=False)
