from setuptools import setup, find_packages

setup(version='0.1.dev0',
      name="astropy-changelog",
      description="Helpers for parsing astropy changelogs",
      url='https://github.com/astrofrog/astropy-changelog',
      packages=find_packages(),
      author='Thomas Robitaille',
      package_data={'astropy_changelog.tests': ['data/*']},
      install_requires=["docutils"])
