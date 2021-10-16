# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest

import foran.cli as cli


def test_cli_main():
    message = 'ignoring template: ignored'
    with pytest.raises(UserWarning) as ex:
        cli.main(['diff', '.', 'foran-eller-bagved.txt', 'ignored']) == 0
        assert message in str(ex.value)


def test_cli_diff_path():
    message = 'ignoring template: ignored'
    with pytest.raises(UserWarning) as ex:
        cli.diff_repo(source=cli.CWD, output='foran-eller-bagved.txt') == 0
        assert message in str(ex.value)


def test_cli_diff_stdout():
    message = 'ignoring template: ignored'
    with pytest.raises(UserWarning) as ex:
        cli.diff_repo(source=cli.CWD) == 0
        assert message in str(ex.value)


def test_cli_label_path():
    message = 'ignoring template: ignored'
    with pytest.raises(UserWarning) as ex:
        cli.label_repo(source=cli.CWD, output='foran-eller-bagved.txt') == 0
        assert message in str(ex.value)


def test_cli_label_stdout():
    message = 'ignoring template: ignored'
    with pytest.raises(UserWarning) as ex:
        cli.label_repo(source=cli.CWD) == 0
        assert message in str(ex.value)
