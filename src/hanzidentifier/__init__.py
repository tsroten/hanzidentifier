"""Python module that identifies Chinese text as Simplified or Traditional."""

from hanzidentifier.core import (
    count_chinese,
    has_chinese,
    identify,
    is_simplified,
    is_traditional,
    BOTH,
    MIXED,
    SIMP,
    SIMPLIFIED,
    TRAD,
    TRADITIONAL,
    UNKNOWN,
)

__version__ = "1.3.0"
