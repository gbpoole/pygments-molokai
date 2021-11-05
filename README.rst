Install
=======

Once you have Pygments installed, you can add the Molokai theme to it as follows...

Using PyPI and pip
------------------

The easiest way is to use 'pip':
::

    $ (sudo) pip install pygments-molokai


Manual
------

For those who want to work from code, you can install the Molokai theme manually.  First make sure that Poetry is installed (see `here`).  Then:
::

    $ git clone git://github.com/gbpoole/pygments-molokai.git
    $ cd pygments-molokai
    $ (sudo) poetry install

.. _here: https://python-poetry.org/docs/#installation

Usage examples
==============

From Python:
::

    >>> from pygments.formatters import HtmlFormatter
    >>> HtmlFormatter(style='molokai').style
    <class 'pygments_style_molokai.MolokaiStyle'>


or from the command line:
::

    pygmentize -g -O style=molokai <FILENAME>

Help
====

More information about Pygment styles can be found at the `official Pygments documentation`_ page.

.. _official documentation: http://pygments.org/docs/

