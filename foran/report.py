# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""In front or behind (Foran eller bagved)? reporting interface."""
import pathlib
from enum import Enum, auto
from typing import Tuple

from foran.status import Status

REPORT_STEM = 'foran-eller-bagved'


class Format(Enum):
    NONE = auto()
    TEXT = auto()


class Report:
    """Report structure."""

    def __init__(self, stem: str = REPORT_STEM, file_format: Format = Format.TEXT):
        """Seed the status structure with the git status info and some defaults."""
        self.stem = stem
        self.file_format = file_format


def report_as(status: Status, report: Report) -> None:
    """Side effects ..."""
    file_extension = '.txt' if report.file_format == Format.TEXT else ''  # TODO(sthagen) HACK A DID ACK
    filepath = pathlib.Path(f'{report.stem}{file_extension}')
    filepath.parent.mkdir(parents=True, exist_ok=True)

    with open(filepath, 'w') as handle:
        handle.write(''.join(generate_report(status)))


def generate_report(status: Status) -> Tuple[str, ...]:
    """Convoluted special trickery ... to build partially conditional report lines"""
    report = []
    report.append(f'Analysis ({status.when})\n')
    report.append(f'State    ({status.foran_disp})\n')
    report.append(f'Branch   ({status.branch})\n')
    report.append(f'Commit   ({status.commit})\n')

    if not status.foran:
        report.append('List of local commits:\n')
        report.append(''.join(f' - {commit}\n' for commit in status.local_commits))

    if status.local_staged:
        report.append('List of locally staged files: \n')
        report.append(''.join(f' - {staged_file}\n' for staged_file in status.local_staged))

    if status.local_files:
        report.append('List of locally modified files: \n')
        report.append(''.join(f' - {mod_file}\n' for mod_file in status.local_files))

    return tuple(report)
