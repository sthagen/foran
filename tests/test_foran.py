# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import foran.foran


def test_main():
    assert foran.main(['argument']) == 0
