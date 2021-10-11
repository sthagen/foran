# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""In front or behind (Foran eller bagved)? API."""
import math
import os
import sys
from enum import Enum, auto
from typing import List, Union

DEBUG_VAR = 'FORAN_DEBUG'
DEBUG = os.getenv(DEBUG_VAR)

ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'


def main(argv: Union[List[str], None] = None) -> int:
    """Drive the analysis."""
    argv = argv if argv else sys.argv[1:]
    if not argv:
        print('ERROR arguments expected.', file=sys.stderr)
        return 2

    return 0
