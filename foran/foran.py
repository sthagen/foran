# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""In front or behind (Foran eller bagved)? API."""
import datetime as dti
import os
import sys
from typing import List, Union

from git import Repo

from foran.report import report_as

DEBUG_VAR = 'FORAN_DEBUG'
DEBUG = os.getenv(DEBUG_VAR)

ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'

Status = dict[str, object]

REPORT_STEM = 'foran-eller-bagved'
REPORT_DTI_FORMAT = '%Y-%m-%d %H:%M:%S UTC'


def git_status(repo: Repo) -> Status:
    """Seed the status structure with the git status info and some defaults."""
    branch_is_up_to_date = 'Your branch is up to date' in repo.git.status()
    return {
        'WHEN': dti.datetime.now(dti.timezone.utc).strftime(REPORT_DTI_FORMAT),
        'BRANCH_NAME': repo.active_branch.name,
        'BRANCH_FORAN': branch_is_up_to_date,
        'BRANCH_FORAN_STR': 'UP TO DATE' if branch_is_up_to_date else 'CUSTOM',
        'COMMIT_ID': repo.head.commit,
        'REPORT_STEM': REPORT_STEM,
    }


def main(argv: Union[List[str], None] = None) -> int:
    """Drive the analysis."""
    argv = argv if argv else sys.argv[1:]
    if not argv:
        print('ERROR arguments expected.', file=sys.stderr)
        return 2

    repo = Repo('.')
    status = git_status(repo)
    report_as(status, repo, 'text/plain')
    return 0
