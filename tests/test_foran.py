# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
from git import Repo

import foran.foran as fb
from foran.status import Status


def test_main():
    assert fb.main(['foran-eller-bagved.functional']) == 0


def test_local_commits():
    repo = Repo('.')
    status = Status(repo)
    status.foran = False
    fb.local_commits(repo, status)
    assert status.local_commits == []
