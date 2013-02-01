ratmodform
==========

Fast research-oriented code for computing with rational modular
forms. Depends on [Sage](http://sagemath.org/).

   https://github.com/williamstein/ratmodform

Released under GPLv2+.

Installing
----------

  Type

     git clone https://github.com/williamstein/ratmodform

  anywhere you want, then type "sage setup.py develop".  You can then
  do "import ratmodform" then "ratmodform.[tab]" in Sage.


  If you are using a Sage install that you can modify, just do the
  following inside the ratmodform directory:

      sage setup.py develop

  NOTE:  To force all modules to rebuild: sage setup.py develop -ba

  If you would like to install ratmodform and you are using a
  system-wide Sage install that you can't modify, you can still do:

    sage setup.py build_ext --inplace

  NOTE: Using virtualenv would be nice here, but Sage doesn't include
  virtualenv.

  You will have to somewhere add your ratmodform directory to sys.path
  to import this module from anywhere.

  import ratmodform

Testing
-------

  Do this to run 8 tests in parallel:

    sage -tp 8 --force_lib ratmodform

  In general, whenever you doctest in psage, do

     sage -t --force_lib

  i.e., use the force_lib option.

