# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pytest
from typer.testing import CliRunner

import foran
import foran.cli as cli
from foran.cli import app
from foran.render import Template

runner = CliRunner()


def test_app_version():
    result = runner.invoke(app, ['version'])
    assert result.exit_code == 0
    assert cli.APP_NAME in result.stdout
    assert foran.__version__ in result.stdout


def test_app_template():
    result = runner.invoke(app, ['template'])
    assert result.exit_code == 0
    assert 'Example template generated per ' in result.stdout


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


def test_cli_classify_template_empty():
    cli.classify_template('') == Template.NONE


def test_cli_classify_template_jinja_string():
    cli.classify_template('{{ JINJA }}') == Template.JINJA_STRING


def test_cli_classify_template_f_string():
    cli.classify_template('{f_string}') == Template.F_STRING


def test_cli_classify_template_jinja_path():
    cli.classify_template('README.md') == Template.JINJA_PATH


def test_cli_classify_template_string():
    cli.classify_template('NOTHING_ELSE_MATTERS') == Template.STRING
