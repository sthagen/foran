# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""In front or behind (Foran eller bagved)? API."""
import os
import pathlib
import warnings
from typing import List, Union

from git import Repo
from git.exc import GitCommandError

from foran.report import Format, Report, report_as
from foran.status import Status

DEBUG_VAR = 'FORAN_DEBUG'
DEBUG = os.getenv(DEBUG_VAR)

ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'


def local_commits(repo: Repo, status: Status) -> None:
    """Yes"""
    if not status.foran:
        branch = repo.active_branch.name
        try:
            status.local_commits = [rev for rev in repo.iter_commits(f'origin/{branch}..{branch}')]
        except GitCommandError as ex:
            symptom = ex.stderr.replace('\n', '')
            if "fatal: bad revision 'origin/default..default'" in symptom:
                warning = 'No remote found, so all commit differences hypothetical'
                status.local_commits = [warning]
                warnings.warn(warning)
            else:
                raise


def local_staged(repo: Repo, status: Status) -> None:
    """Truly"""
    status.local_staged = [item.a_path for item in repo.index.diff('HEAD')]


def local_files(repo: Repo, status: Status) -> None:
    """Sure"""
    status.local_files = [item.a_path for item in repo.index.diff(None)]


def main(argv: Union[List[str], None] = None) -> int:
    """Drive the analysis."""
    # [('diff'|'label'), repo_root, target, template]
    if not argv or len(argv) != 4:
        warnings.warn('received wrong number of arguments')
        return 2

    if argv[0] not in ('diff', 'label'):
        warnings.warn('received unknown command')
        return 2

    command, repo_root, target, template = argv

    if not pathlib.Path(str(repo_root)).is_dir():
        warnings.warn('repository root is no directory')
        return 1

    if template and target != 'STD_OUT':
        warnings.warn('templates not yet implemented')

    report = Report(stem=target, file_format=Format.NONE)

    repo = Repo(repo_root)
    status = Status(repo)
    if command == 'diff':
        local_commits(repo, status)
        local_staged(repo, status)
        local_files(repo, status)
    report_as(status, report)
    return 0
