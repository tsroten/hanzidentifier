# -*- coding: utf-8 -*-
import re

from zhon import cedict

TRADITIONAL_CHARACTERS = set(list(cedict.traditional))
SIMPLIFIED_CHARACTERS = set(list(cedict.simplified))
SHARED_CHARACTERS = TRADITIONAL_CHARACTERS & SIMPLIFIED_CHARACTERS
ALL_CHARACTERS = cedict.all
HANZI_MATCH = re.compile(f"[^{ALL_CHARACTERS}]")


def get_hanzi(s):
    """Extract a string's Chinese characters."""
    return set(HANZI_MATCH.sub("", s))
