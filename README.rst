About
-----

.. image:: https://github.com/astropy/astropy-changelog/workflows/CI/badge.svg
    :alt: CI Status
    :target: https://github.com/astropy/astropy-changelog/actions

.. image:: https://codecov.io/gh/astropy/astropy-changelog/branch/main/graph/badge.svg
    :alt: Coverage
    :target: https://codecov.io/gh/astropy/astropy-changelog

To install::

    pip install astropy-changelog

This package contains a parser for the Astropy changelog format. Example usage:

.. code:: python

    In [1]: from astropy_changelog import load

    In [2]: changes = load('CHANGES.rst')

    In [3]: changes.versions
    Out[3]:
    ['0.1',
     '0.2',
     '0.2.1',
     '0.2.2',
     '0.2.3',
     ...]

    In [4]: changes.issues
    Out[4]:
    [256,
     272,
     291,
     293,
     296,
     ...]

    In [5]: changes.versions_for_issue(4242)
    Out[5]: ['1.2']

    In [6]: changes.issues_for_version('2.0.7')
    Out[6]: [7411, 7248, 7402, 7422, 7469, 7486, 7453, 7493, 7510, 7493]

Format specification
--------------------

The current format uses reStructuredText. Changelog entries should be given as
bullet point items inside sections for each version. These sections should have
a title with the following syntax::

    version (release date)

The release date can be ``unreleased`` if the version is not released yet.

The version sections can optionally include sub-sections in which the bullet
items are organized, and the file can also optionally include an overall title.
