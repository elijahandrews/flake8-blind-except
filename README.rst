flake8-blind-except
===================

A flake8 extension that checks for blind ``except:`` statements.

Using ``except`` without explicitly specifying which exceptions to catch is generally considered back practice.

An example of code that will fail this check is::

    try:
        something_scary()
    except:
        everybody_panic()

However, the following code is valid::

    try:
        something_terrifying()
    except Exception:
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



Changes
------

0.1.03 - 2014-02-07
``````````````````
* Initial release

Notes
-----

I've tested this package with flake8 2.0 and Python 2.7. It is untested, but likely compatible with other versions.
