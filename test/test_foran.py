# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring,unused-import,reimported
import pathlib

import pytest
from git import Repo
from git.exc import InvalidGitRepositoryError

import foran.foran as fb
from foran.status import Status


def test_main_empty():
    message = 'received wrong number of arguments'
    with pytest.raises(UserWarning) as ex:
        fb.main([]) == 2
        assert message in str(ex.value)


def test_main_few():
    message = 'received wrong number of arguments'
    with pytest.raises(UserWarning) as ex:
        fb.main(['diff', '.', 'would_be_here']) == 2
        assert message in str(ex.value)


def test_main_unknown_command():
    message = 'received unknown command'
    with pytest.raises(UserWarning) as ex:
        fb.main(['unknown', '.', 'would_be_here', '']) == 2
        assert message in str(ex.value)


def test_main_diff():
    assert fb.main(['diff', '.', 'foran-eller-bagved.txt', '']) == 0


def test_main_label():
    assert fb.main(['label', '.', 'STD_OUT', '']) == 0


def test_main_template():
    message = 'ignoring template: ignored'
    with pytest.raises(UserWarning) as ex:
        fb.main(['diff', '.', 'foran-eller-bagved.txt', 'ignored']) == 0
        assert message in str(ex.value)


def test_local_commits_none():
    repo = Repo('.')
    status = Status(repo)
    status.foran = True
    fb.local_commits(repo, status)
    assert status.local_commits == []


def test_local_commits_some():
    repo = Repo('.')
    status = Status(repo)
    status.foran = False
    fb.local_commits(repo, status)
    assert len(status.local_commits) == 6


def test_local_commits_no_repo():
    with pytest.raises(InvalidGitRepositoryError):
        _ = Repo('test')
        # We cannot currently really probe for a git repo that raises GitCommandError


def test_local_commits_no_remote():
    path_to_non_remote = pathlib.Path('test', 'fixtures', 'non_remote')
    repo = Repo(path_to_non_remote)
    status = Status(repo)
    status.foran = False
    message = 'No remote found, so all commit differences hypothetical'
    with pytest.raises(UserWarning) as ex:
        fb.local_commits(repo, status)
        assert status.local_commits == [message]
        assert message in str(ex.value)
