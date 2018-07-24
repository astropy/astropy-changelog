# A validator for the Astropy reStructuredText changelog format

import re
import docutils.nodes
import docutils.parsers.rst
import docutils.utils

VERSION_PATTERN = re.compile('^v?[0-9\.]+ \([\w\-]+\)')
BLOCK_PATTERN = re.compile('\[#.+\]', flags=re.DOTALL)
ISSUE_PATTERN = re.compile('#[0-9]+')


def find_prs_in_entry(content):
    issue_numbers = []
    for block in BLOCK_PATTERN.finditer(content):
        block_start, block_end = block.start(), block.end()
        block = content[block_start:block_end]
        for m in ISSUE_PATTERN.finditer(block):
            start, end = m.start(), m.end()
            issue_numbers.append(int(block[start:end][1:]))
    return issue_numbers


class BulletItemVisitor(docutils.nodes.NodeVisitor):

    def __init__(self, document, warn):
        super(BulletItemVisitor, self).__init__(document)
        self.warn = warn
        self.reset_bullet_items()

    def reset_bullet_items(self):
        self.bullet_items = []

    def dispatch_visit(self, node):
        if isinstance(node, docutils.nodes.list_item):
            self.bullet_items.append(node)
            raise docutils.nodes.SkipChildren
        elif isinstance(node, (docutils.nodes.title, docutils.nodes.system_message)):
            raise docutils.nodes.SkipChildren
        elif isinstance(node, (docutils.nodes.section, docutils.nodes.bullet_list)):
            pass
        else:
            self.warn('Unexpected content: {0}'.format(node.astext()))


class AstropyChangelog:

    def warn(self, message):
        print('WARNING:', message)

    def _validate_version(self, string):
        if VERSION_PATTERN.match(string) is None:
            self.warn("Invalid version string: {0}".format(string))

    def _parse_observer(self, data):
        if data['level'] > 1:
            self.warn(data.children[0].astext())
        return data

    def parse(self, filename):

        # Open file and read contents

        with open(filename) as f:
            text = f.read()

        # Parse as rst

        parser = docutils.parsers.rst.Parser()
        components = (docutils.parsers.rst.Parser,)
        settings = docutils.frontend.OptionParser(components=components).get_default_values()
        document = docutils.utils.new_document('<rst-doc>', settings=settings)
        document.reporter.stream = None
        document.reporter.attach_observer(self._parse_observer)
        parser.parse(text, document)

        # At the top level, the document should just include sections whose name is
        # a version number followed by a release date.

        visitor = BulletItemVisitor(document, self.warn)

        self._issues_by_version = {}

        for section in document:

            title = section.attributes['names'][0]
            self._validate_version(title)

            # Inside each version section there may either directly be a list of
            # entries, or more nested sections. We use a visitor class to search
            # for all the bullet point entries, and in the process we make sure
            # that there are only section titles and bullet point entries in the
            # section

            visitor.reset_bullet_items()
            section.walk(visitor)

            # Go over the bullet point items and find the PR numbers
            issues = []
            for item in visitor.bullet_items:
                issues.extend(find_prs_in_entry(item.astext()))

        self.document = document

        return document


if __name__ == '__main__':
    parser = ChangelogParser()
    parser.validate('CHANGES.rst')
