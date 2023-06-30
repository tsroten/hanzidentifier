# -*- coding: utf-8 -*-
from hanzidentifier import helpers

UNKNOWN = 0
TRAD = TRADITIONAL = 1
SIMP = SIMPLIFIED = 2
BOTH = 3
MIXED = 4


def identify(s):
    """Identify what kind of Chinese characters a string contains.

    *s* is a string to examine. The string's Chinese characters are tested to
    see if they are compatible with the Traditional or Simplified characters
    systems, compatible with both, or contain a mixture of Traditional and
    Simplified characters. The :data:`TRADITIONAL`, :data:`SIMPLIFIED`,
    :data:`BOTH`, or :data:`MIXED` constants are returned to indicate the
    string's identity. If *s* contains no Chinese characters, then
    :data:`UNKNOWN` is returned.

    All characters in a string that aren't found in the CC-CEDICT dictionary
    are ignored.

    Because the Traditional and Simplified Chinese character systems overlap, a
    string containing Simplified characters could identify as
    :data:`SIMPLIFIED` or :data:`BOTH` depending on if the characters are also
    Traditional characters. To make testing the identity of a string easier,
    the functions :func:`is_traditional`, :func:`is_simplified`, and
    :func:`has_chinese` are provided.

    """
    chinese = helpers.get_hanzi(s)
    if not chinese:
        return UNKNOWN
    if chinese.issubset(helpers.SHARED_CHARACTERS):
        return BOTH
    if chinese.issubset(helpers.TRADITIONAL_CHARACTERS):
        return TRADITIONAL
    if chinese.issubset(helpers.SIMPLIFIED_CHARACTERS):
        return SIMPLIFIED
    return MIXED


def has_chinese(s):
    """Check if a string has Chinese characters in it.

    This is a faster version of:
        >>> identify('foo') is not UNKNOWN

    """
    return bool(helpers.get_hanzi(s))


def is_traditional(s):
    """Check if a string's Chinese characters are Traditional.

    This is equivalent to:
        >>> identify('foo') in (TRADITIONAL, BOTH)

    """
    chinese = helpers.get_hanzi(s)
    if not chinese:
        return False
    if chinese.issubset(helpers.SHARED_CHARACTERS):
        return True
    if chinese.issubset(helpers.TRADITIONAL_CHARACTERS):
        return True
    return False


def is_simplified(s):
    """Check if a string's Chinese characters are Simplified.

    This is equivalent to:
        >>> identify('foo') in (SIMPLIFIED, BOTH)

    """
    chinese = helpers.get_hanzi(s)
    if not chinese:
        return False
    if chinese.issubset(helpers.SHARED_CHARACTERS):
        return True
    if chinese.issubset(helpers.SIMPLIFIED_CHARACTERS):
        return True
    return False


def count_chinese(s: str) -> int:
    """count how many chinese exist in a string"""
    result = 0
    for i in s:
        if has_chinese(i):
            result += 1
    return result
