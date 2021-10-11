# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""In front or behind (Foran eller bagved)? reporting interface."""
import pathlib

from git import Repo

Status = dict[str, object]


def report_as(status: Status, repo: Repo, format: str) -> None:
    """Side effects ..."""
    file_extension = '.txt' if format == 'text/plain' else ''  # TODO(sthagen) HACK A DID ACK
    filepath = pathlib.Path(f"{status['REPORT_STEM']}{file_extension}")
    filepath.parent.mkdir(parents=True, exist_ok=True)

    with open(filepath, 'w') as handle:
        handle.write(''.join(generate_report(repo, status)))


def generate_report(repo: Repo, status: Status) -> tuple[str, ...]:
    """Convoluted special trickery ... to build partially conditional report lines"""
    report = []
    report.append(f"Analysis ({status['WHEN']})\n")
    report.append(f"State    ({status['BRANCH_FORAN_STR']})\n")
    report.append(f"Branch   ({status['BRANCH_NAME']})\n")
    report.append(f"Commit   ({status['COMMIT_ID']})\n")

    if not status['BRANCH_FORAN']:
        active_branch_name = repo.active_branch.name
        unpushed_commits = [rev for rev in repo.iter_commits(f'origin/{active_branch_name}..{active_branch_name}')]
        report.append('List of local commits:\n')
        report.append(''.join(f' - {commit}\n' for commit in unpushed_commits))

    modified_files = [item.a_path for item in repo.index.diff(None)]
    if modified_files:
        report.append('List of locally modified files: \n')
        report.append(''.join(f' - {mod_file}\n' for mod_file in modified_files))

    return tuple(report)
