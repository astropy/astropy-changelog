from astropy_changelog.rst_parser import AstropyRstChangelog

__all__ = ['parse']


def parse(filename, format='rst'):
    """
    Parse a changelog file.

    Parameters
    ----------
    filename : str
        The changelog file
    format : { 'rst' }
        The format of the changelog file (only rst is supported at this time)
    title : bool
        Whether an overall title is present
    """
    if format == 'rst':
        changelog = AstropyRstChangelog()
        changelog.parse(filename)
        return changelog
    else:
        raise ValueError('Format not recognized: {0}'.format(format))
