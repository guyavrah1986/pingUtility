from setuptools import setup, find_packages

setup(name="pingUtility",
      version="1.0",
      description="Basic ping utility that sends constantly at pre-defined intervals ping requests towards an IP address" ,
      url="https://github.com/guyavrah1986/pingUtility",
      author="Guy Avraham",
      author_email="guyavrah1986@gmail.com",
      license="MIT",
      packages=find_packages(),
      include_package_data=True,
      install_requires=['ping3'])
