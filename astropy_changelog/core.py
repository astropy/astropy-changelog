from astropy_changelog.rst_parser import AstropyRstChangelog

__all__ = ['load', 'loads']


def load(filename, format='rst'):
    """
    Parse a changelog file.

    Parameters
    ----------
    filename : str
        The changelog file
    format : { 'rst' }
        The format of the changelog file (only rst is supported at this time)
    """
    if format == 'rst':
        changelog = AstropyRstChangelog()
        changelog.parse_file(filename)
        return changelog
    else:
        raise ValueError('Format not recognized: {0}'.format(format))


def loads(text, format='rst'):
    """
    Parse a changelog string.

    Parameters
    ----------
    text : str
        The changelog string
    format : { 'rst' }
        The format of the changelog file (only rst is supported at this time)
    """
    if format == 'rst':
        changelog = AstropyRstChangelog()
        changelog.parse_string(text)
        return changelog
    else:
        raise ValueError('Format not recognized: {0}'.format(format))
