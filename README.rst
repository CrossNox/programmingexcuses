ProgrammingExcuses
==================

Tired of making up your own excuses? Get them from
http://programmingexcuses.com with python!

Installing
==========

``pip install programmingexcuses``

Testing
=======

.. code:: bash

   $ programmingexcuse
   Management insisted we wouldn't need to waste our time writing unit tests

Usage
=====

It’s quite simple:

.. code:: python

   from programmingexcuses import get_excuse
   print(get_excuse())

And, for convenience:

.. code:: python

   from programmingexcuses import RandomExcuseError
   try:
       ...
   except:
       raise RandomExcuseError()

Also, from a terminal:

.. code:: bash

   programmingexcuse
