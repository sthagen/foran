# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""In front or behind (Foran eller bagved)? API."""
import os
import sys
from typing import List, Union

from git import Repo

from foran.report import Report, report_as
from foran.status import Status

DEBUG_VAR = 'FORAN_DEBUG'
DEBUG = os.getenv(DEBUG_VAR)

ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'


def local_commits(repo: Repo, status: Status) -> None:
    """Yes"""
    if not status.foran:
        branch = repo.active_branch.name
        status.local_commits = [rev for rev in repo.iter_commits(f'origin/{branch}..{branch}')]


def local_files(repo: Repo, status: Status) -> None:
    """Sure"""
    status.local_files = [item.a_path for item in repo.index.diff(None)]


def main(argv: Union[List[str], None] = None) -> int:
    """Drive the analysis."""
    argv = argv if argv else sys.argv[1:]
    repo = Repo('.')
    status = Status(repo)
    local_commits(repo, status)
    local_files(repo, status)
    report = Report()
    report_as(status, report)
    return 0
