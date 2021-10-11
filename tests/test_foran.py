# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import foran.foran as fb


def test_main():
    assert fb.main(['argument']) == 0
