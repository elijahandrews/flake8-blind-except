flake8-blind-except
===================

A flake8 extension that checks for blind, catch-all ``except:`` and ``except Exception:`` statements.

As of `pycodestyle 2.1.0 <https://github.com/PyCQA/pycodestyle/commit/543f12b06592c53e2e60edc4846ee02ab9550e8b/>`_, "E722 do not use bare except, specify exception instead" is built-in. However, bare ``Exception`` and ``BaseException`` are still allowed. This extension flags them as `B902`.

Using ``except`` without explicitly specifying which exceptions to catch is generally considered bad practice, since it catches system signals like ``SIGINT``. You probably want to handle system interrupts differently than exceptions occuring in your code.

It's also usually better style to have many small ``try``-``except`` blocks catching specific exceptions instead of a giant ``try:`` block with a catch-all ``except:`` at the bottom. It's also nicer to your fellow programmers to be a bit more specific about what exceptions they can expect in specific parts of the code, and what the proper course of action is when they occur.

An example of code that will fail this check is:

.. code-block:: python

    try:
        something_scary()
    except:
        everybody_panic()

However, the following code is valid:

.. code-block:: python

    try:
        something_terrifying()
    except TerrifyingException:
        dont_panic()

Installation
------------

If you don't already have it, install ``flake8``::

    $ pip install flake8

Then, install the extension::

    $ pip install flake8-blind-except

Usage
-----

Run the following to verify that the plugin has been installed correctly::

    $ flake8 --version
    2.0 (pep8: 1.4.6, flake8-blind-except: 0.1.0, pyflakes: 0.7.3)

Now, when you run ``flake8``, the plugin will automatically be used.

When a blind except is found, ``flake8`` will output::

    B901 blind except: statement

or::

    B902 blind except Exception: statement

Contributing
------------

I'm not working on Python these days, so probably won't be making updates anytime soon. PRs are welcome though!

Testing
-------

Tests can be run with ``pytest --doctest-modules flake8_blind_except.py``.

Changes
-------

0.2.0 - 2021-01-07
``````````````````
* B902 error added for cases where a blind ``Exception`` is caught.

0.1.1 - 2016-06-27
``````````````````
* ``pep8`` was renamed to ``pycodestyle`` in its 2.0 release. Compatibility update for this change.

0.1.0 - 2014-02-07
``````````````````
* Initial release

Notes
-----

I've tested this package with flake8 2.6.2 + Python 2.7.3 and flake8 3.7.9 + Python 3.7.5.
