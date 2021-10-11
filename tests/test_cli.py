# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import foran.cli as cli


def test_cli():
    assert cli.main(['foran-eller-bagved.txt']) == 0
