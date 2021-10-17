# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
from foran.report import generate_report_list


def test_generate_report_list_nothing_ast_empty():
    assert generate_report_list('foo:', False, [], '*') == []


def test_generate_report_list_ast_empty():
    assert generate_report_list('', True, [], '*') == ['\n']


def test_generate_report_list_default_single():
    assert generate_report_list('foo:', True, ['bar']) == ['foo:\n', ' * bar\n']


def test_generate_report_list_ast_single():
    assert generate_report_list('foo:', True, ['bar'], '*') == ['foo:\n', ' * bar\n']


def test_generate_report_list_plus_single():
    assert generate_report_list('foo:', True, ['bar'], '+') == ['foo:\n', ' + bar\n']


def test_generate_report_list_dash_single():
    assert generate_report_list('foo:', True, ['bar'], '-') == ['foo:\n', ' - bar\n']


def test_generate_report_list_default_two():
    assert generate_report_list('foo:', True, ['bar', 'baz']) == ['foo:\n', ' * bar\n * baz\n']


def test_generate_report_list_nothing_default_two():
    assert generate_report_list('foo:', False, ['bar', 'baz']) == []
