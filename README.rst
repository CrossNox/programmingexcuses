ProgrammingExcuses
==================

Tired of making up your own excuses? Get them from
http://programmingexcuses.com with python!

Installing
==========

``pip install programmingexcuses``

Testing
=======

There are no tests! I was gonna make up an excuse for that but this
package does it for me :D

.. code:: bash

   $ programmingexcuse
   Management insisted we wouldn't need to waste our time writing unit tests

Usage
=====

It’s quite simple:

.. code:: python

   import programmingexcuses
   print(programming_excuses.get_excuse())

And, for convenience:

.. code:: python

   import programmingexcuses
   try:
       ...
   except:
       raise RandomExcuseError()

Also, from a terminal:

.. code:: bash

   programmingexcuse
