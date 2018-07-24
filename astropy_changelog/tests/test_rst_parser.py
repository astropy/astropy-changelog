import os
from astropy_changelog import parse

DATA = os.path.join(os.path.dirname(__file__), 'data')


def test_rst_parser():

    changelog = parse(os.path.join(DATA, 'changes_core.rst'))

    assert changelog.versions == ['0.1', '3.0.1', '3.1']

    assert changelog.issues == [100, 102, 103, 104, 105, 106, 107, 108, 109]

    assert changelog.issues_for_version('0.1') == []
    assert changelog.issues_for_version('3.0.1') == [104, 105, 106, 107, 108, 109]
    assert changelog.issues_for_version('3.1') == [100, 102, 103]

    for issue in [104, 105, 106, 107, 108, 109]:
        assert changelog.versions_for_issue(issue) == ['3.0.1']

    for issue in [100, 102, 103]:
        assert changelog.versions_for_issue(issue) == ['3.1']
