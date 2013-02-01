#################################################################################
#
# (c) Copyright 2013 William Stein
#
#  This is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 2 of the License, or
#  (at your option) any later version.
#
#  This is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#################################################################################

import os, sys
import build_system

SAGE_ROOT  = os.environ['SAGE_ROOT']
SAGE_LOCAL = os.environ['SAGE_LOCAL']

INCLUDES = ['%s/%s/'%(SAGE_ROOT,x) for x in
             ('devel/sage/sage/ext', 'devel/sage', 'devel/sage/sage/gsl')] \
         + ['%s/%s/'%(SAGE_LOCAL,x) for x in
             ('include/csage', 'include', 'include/python')]

if '-ba' in sys.argv:
    print "Rebuilding all Cython extensions."
    sys.argv.remove('-ba')
    FORCE = True
else:
    FORCE = False

def Extension(*args, **kwds):
    if not kwds.has_key('include_dirs'):
        kwds['include_dirs'] = INCLUDES
    else:
        kwds['include_dirs'] += INCLUDES
    if not kwds.has_key('force'):
        kwds['force'] = FORCE

    # Disable warnings when running GCC step -- cython has already parsed the code and
    # generated any warnings; the GCC ones are noise.
    if not kwds.has_key('extra_compile_args'):
        kwds['extra_compile_args'] = ['-w']
    else:
        kwds['extra_compile_args'].append('-w')

    E = build_system.Extension(*args, **kwds)
    E.libraries = ['csage'] + E.libraries
    return E


numpy_include_dirs = [os.path.join(SAGE_LOCAL,
                                   'lib/python/site-packages/numpy/core/include')]

ext_modules = [
    Extension("ratmodform.misc_list", ["ratmodform/misc_list.pyx"]),

    Extension("ratmodform.special_fast",
              ["ratmodform/special_fast.pyx", SAGE_ROOT + "/devel/sage/sage/libs/flint/fmpq_poly.c"],
              libraries = ['gmp', 'flint'],
              language = 'c++',
              include_dirs = [SAGE_LOCAL + '/include/FLINT/', SAGE_ROOT + '/devel/sage/sage/libs/flint/'],
              extra_compile_args = ['-std=c99']),

]

# I just had a long chat with Robert Bradshaw (a Cython dev), and he
# told me the following functionality -- turning an Extension with
# Cython code into one without -- along with proper dependency
# checking, is now included in the latest development version of
# Cython (Nov 2, 2010).  It's supposed to be a rewrite he did of the
# code in the Sage library.  Hence once that gets released, we should
# switch to using it here.

build_system.cythonize(ext_modules)

build_system.setup(
    name = 'ratmodform',
    version = "2013.01.31",
    description = "Fast research-oriented code for computing with rational modular forms. Depends on Sage.",
    author = 'William Stein',
    author_email = 'wstein@gmail.com',
    url = 'https://github.com/williamstein/ratmodform',
    license = 'GPL v2+',
    packages = ['ratmodform'],
    platforms = ['any'],
    download_url = 'NA',
    ext_modules = ext_modules
)

