# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pathlib

import pytest
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


def test_local_commits_no_remote():
    path_to_non_remote = pathlib.Path('tests', 'fixtures', 'non_remote')
    repo = Repo(path_to_non_remote)
    status = Status(repo)
    status.foran = False
    message = 'No remote found, so all commit differences hypothetical'
    with pytest.raises(UserWarning) as ex:
        fb.local_commits(repo, status)
        assert status.local_commits == [message]
        assert message in str(ex.value)
