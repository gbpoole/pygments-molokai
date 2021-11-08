=======================
Pygments Molokai Plugin
=======================

This Python package can be used to add the Molokai colour theme to Pygments.  It was generated from the `Vim
Molokai plugin`_ using the `Vim Colorscheme Converter`_.

.. _`Vim Molokai plugin`: https://github.com/tomasr/molokai

.. _`Vim Colorscheme Converter`: https://github.com/honza/vim2pygments

Install
=======

Once you have Pygments installed, you can add the Molokai theme to it as follows...

Using PyPI and pip
------------------

The easiest way is to use 'pip':
::

    $ pip install pygments_molokai


Manual
------

For those who want to work from code, you can install the Molokai theme manually.  First make sure that Poetry is installed (see `here`).  Then:
::

    $ git clone git://github.com/gbpoole/pygments-molokai.git
    $ cd pygments-molokai
    $ poetry install

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

More information about Pygment styles can be found at the `official Pygments documentation` page.

.. _official documentation: http://pygments.org/docs/

