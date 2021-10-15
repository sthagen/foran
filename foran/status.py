# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""In front or behind (Foran eller bagved)? status structure."""
import datetime as dti

from git import Repo

STATUS_DTI_FORMAT = '%Y-%m-%d %H:%M:%S UTC'


class Status:
    """Status structure."""

    def __init__(self, repo: Repo, timestamp_format: str = STATUS_DTI_FORMAT):
        """Seed the status structure with the git status info and some defaults."""
        self._repo = repo
        branch_is_up_to_date = 'Your branch is up to date' in self._repo.git.status()
        self.when = dti.datetime.now(dti.timezone.utc).strftime(timestamp_format)
        self.branch = self._repo.active_branch.name
        self.foran = branch_is_up_to_date
        self.foran_disp = 'UP TO DATE' if branch_is_up_to_date else 'CUSTOM'
        self.commit = self._repo.head.commit
        self.local_commits: list[str] = []
        self.local_staged: list[str] = []
        self.local_files: list[str] = []
