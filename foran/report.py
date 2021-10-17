# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""In front or behind (Foran eller bagved)? reporting interface."""
import pathlib
from enum import Enum, auto
from typing import List, Tuple

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
    if report.stem == 'STD_OUT':
        print(''.join(generate_report(status)))
        return

    file_extension = '.txt' if report.file_format == Format.TEXT else ''  # TODO(sthagen) HACK A DID ACK
    filepath = pathlib.Path(f'{report.stem}{file_extension}')
    filepath.parent.mkdir(parents=True, exist_ok=True)

    with open(filepath, 'w') as handle:
        handle.write(''.join(generate_report(status)))


def generate_report_list(label: str, anything: bool, entries: List[str], list_symbol: str = '*') -> list[str]:
    """Generic list report generator."""
    if not anything:
        return []
    if not entries:
        return [f'{label}\n']

    return [f'{label}\n'] + [''.join(f' {list_symbol} {entry}\n' for entry in entries)]


def generate_report(status: Status) -> Tuple[str, ...]:
    """Convoluted special trickery ... to build partially conditional report lines"""
    report = []
    report.append(f'Analysis ({status.when})\n')
    report.append(f'State    ({status.foran_disp})\n')
    report.append(f'Branch   ({status.branch})\n')
    report.append(f'Commit   ({status.commit})\n')

    report += generate_report_list('List of local commits:', not status.foran, status.local_commits, '*')
    report += generate_report_list('List of locally staged files:', bool(status.local_staged), status.local_staged, '+')
    report += generate_report_list('List of locally modified files:', bool(status.local_files), status.local_files, '-')

    return tuple(report)
