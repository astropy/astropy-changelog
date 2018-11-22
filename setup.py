from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = f.read()

setup(version='0.1.dev0',
      name="astropy-changelog",
      description="Helpers for parsing astropy changelogs",
      long_description=long_description,
      url='https://github.com/astrofrog/astropy-changelog',
      packages=find_packages(),
      author='Thomas Robitaille',
      author_email='thomas.robitaille@gmail.com',
      package_data={'astropy_changelog.tests': ['data/*']},
      extras_require={'test': ['pytest>=3.5', 'pytest-flake8', 'pytest-cov', 'codecov']},
      install_requires=["docutils"])
