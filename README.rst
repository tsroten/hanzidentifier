Hanzi Identifier
================

About
-----

Hanzi Identifier is a simple Python module that identifies a string of text has having Simplified or Traditional characters.

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
``hanzidentifer.SIMPLIFIED`` or ``hanzidentifier.BOTH`` depending on if the
characters are also Traditional characters.

Hanzi Identifier's functions accept and return unicode.

Install
-------

Hanzi Identifier runs on Python 2.7 and 3. It requires `Zhon <https://github.com/tsroten/zhon>`_ to run.

.. code:: bash

    $ pip install hanzidentifer

Bugs/Feature Requests
---------------------

Hanzi Identifier uses its `GitHub Issues page
<https://github.com/tsroten/hanzidentifer/issues>`_ to track bugs, feature
requests, and support questions.

Change Log
----------

v1.0 (2014-04-12)
~~~~~~~~~~~~~~~~~

Version 1.0 merges some changes from Dragon Mapper. It is not backwards compatible with
the previous versions of Hanzi Identifier (e.g. some of the constants are named differently).

* Merges code from `Dragon Mapper <http://github.com/tsroten/dragonmapper>`_ project.
* Adds tox support.

v0.1 (2013-04-24)
~~~~~~~~~~~~~~~~~

* Initial release.

License
-------

Hanzi Identifier is released under the OSI-approved `MIT License <http://opensource.org/licenses/MIT>`_. See the file `LICENSE.txt` for more information.
