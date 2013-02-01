ratmodform
==========

Fast research-oriented code for computing with rational modular
forms. Depends on [Sage](http://sagemath.org).

   https://github.com/williamstein/ratmodform

Released under GPLv2+.

Installing
----------

  Type

     git clone https://github.com/williamstein/ratmodform

  anywhere you want, then type "sage setup.py develop".  You can then
  do "import ratmodform" then "ratmodform.[tab]" in Sage.

  To build in place just do the following inside the ratmodform directory:

      sage setup.py develop

  To force all modules to rebuild do:

      sage setup.py develop -ba

Testing
-------

  Do this to run 8 tests in parallel:

    sage -tp 8 --force_lib ratmodform

  In general, whenever you doctest in psage, do

     sage -t --force_lib

  i.e., use the force_lib option.

