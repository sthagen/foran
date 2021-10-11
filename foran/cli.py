#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Commandline API gateway for foran."""
import sys
from typing import List, Union

import foran.foran as fb


# pylint: disable=expression-not-assigned
def main(argv: Union[List[str], None] = None) -> int:
    """Delegate processing to functional module."""
    argv = sys.argv[1:] if argv is None else argv
    return fb.main(argv)
