================
Hanzi Identifier
================

.. image:: https://badge.fury.io/py/hanzidentifier.svg
    :target: https://pypi.org/project/hanzidentifier

.. image:: https://github.com/tsroten/hanzidentifier/actions/workflows/ci.yml/badge.svg
    :target: https://github.com/tsroten/hanzidentifier/actions/workflows/ci.yml

Hanzi Identifier is a simple Python module that identifies a string of text as 
having Simplified or Traditional characters.

* GitHub: https://github.com/tsroten/hanzidentifier
* Free software: MIT license

About
-----

Easy-to-use helper functions for identifying strings:

.. code:: python

    >>> import hanzidentifier
    >>> hanzidentifier.has_chinese('Hello my name is John.')
    False
    >>> hanzidentifier.is_simplified('John说：你好！')
    True
    >>> hanzidentifier.is_traditional('John說：你好！')
    True
    >>> hanzidentifier.has_chinese('Country in Simplified: 国家. Country in Traditional: 國家.')
    True

Here it is without the helper functions:

.. code:: python

    >>> hanzidentifier.identify('Hello my name is Thomas.') is hanzidentifier.UNKNOWN
    True
    >>> hanzidentifier.identify('Thomas 说：你好！') is hanzidentifier.SIMPLIFIED
    True
    >>> hanzidentifier.identify('Thomas 說：你好！') is hanzidentifier.TRADITIONAL
    True
    >>> hanzidentifier.identify('你好！') is hanzidentifier.BOTH
    True
    >>> hanzidentifier.identify('Country in Simplified: 国家. Country in Traditional: 國家.' ) is hanzidentifier.MIXED
    True

``hanzidentifier.identify`` has five possible return values:

* ``hanzidentifier.UNKNOWN``: there are no recognized Chinese characters in the string.
* ``hanzidentifier.BOTH``: the string is compatible with both Simplified and Traditional character systems.
* ``hanzidentifier.TRADITIONAL``: the string consists of Traditional characters.
* ``hanzidentifier.SIMPLIFIED``: the string consists of Simplified characters.
* ``hanzidentifier.MIXED``: the string consists of characters recognized solely as Traditional characters and also consists of characters recognized solely as Simplified characters.

Characters that aren't found in CC-CEDICT are ignored when determining a string's identity.
Hanzi Identifier uses the CC-CEDICT data provided by `Zhon <https://github.com/tsroten/zhon>`_ to identify Chinese characters.

Because the Traditional and Simplified Chinese character systems overlap, a
string containing Simplified characters could identify as
``hanzidentifier.SIMPLIFIED`` or ``hanzidentifier.BOTH`` depending on if the
characters are also Traditional characters.

Getting Started
---------------

* Install Hanzi Identifier: ``$ pip install hanzidentifier``
* Report bugs and ask questions via `GitHub Issues <https://github.com/tsroten/hanzidentifier/issues>`_
* `Contribute features or bug fixes <https://github.com/tsroten/hanzidentifier/pulls>`_