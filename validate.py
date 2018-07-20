# A validator for the Astropy reStructuredText changelog format

import re
import docutils.nodes
import docutils.parsers.rst
import docutils.utils

VERSION_PATTERN = re.compile('^v?[0-9\.]+ \([\w\-]+\)')


class ChangelogParser:

    def warn(self, message):
        print('WARNING:', message)

    def validate(self, filename):

        document = self.parse(filename)

        # At the top level, the document should just include sections whose name is
        # a version number followed by a release date.

        for section in document:
            title = section.attributes['names'][0]
            self._validate_version(title)

    def _validate_version(self, string):
        if VERSION_PATTERN.match(string) is None:
            self.warn("Invalid version string: {0}".format(string))

    def _parse_observer(self, data):
        if data['level'] > 1:
            self.warn(data.children[0].astext())
        return data

    def parse(self, filename):
        with open(filename) as f:
            text = f.read()
        parser = docutils.parsers.rst.Parser()
        components = (docutils.parsers.rst.Parser,)
        settings = docutils.frontend.OptionParser(components=components).get_default_values()
        document = docutils.utils.new_document('<rst-doc>', settings=settings)
        document.reporter.stream = None
        document.reporter.attach_observer(self._parse_observer)
        parser.parse(text, document)
        return document


if __name__ == '__main__':
    parser = ChangelogParser()
    parser.validate('CHANGES.rst')
