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
===========

Coming soon

Usage
====

Coming soon

Changes
======

Coming soon
