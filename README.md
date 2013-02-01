ratmodform
==========

Fast research-oriented code for computing with rational modular forms. Depends on Sage.

   https://github.com/williamstein/ratmodform

Released under GPLv2+.

BUILDING:

  To build in place just do:

      sage setup.py develop

  To force all modules to rebuild do:

      sage setup.py develop -ba

DOCTESTS:

  Do this to run 8 tests in parallel:

    sage -tp 8 --force_lib ratmodform

  In general, whenever you doctest in psage, do

     sage -t --force_lib

  i.e., use the force_lib option.

