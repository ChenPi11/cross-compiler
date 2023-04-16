#!/usr/bin/env python3
import os
import sys
CONFIGURE=sys.argv[1]
PROFILES=sys.argv[2]
HOST=sys.argv[3]
BUILDDIR=sys.argv[4]
INSTALL_PREFIX=sys.argv[5]
MAKE_PROFILES=sys.argv[6]
try:
    os.makedirs(BUILDDIR)
except FileExistsError:
    pass
os.chdir(BUILDDIR)
r=0
os.system(f"make clean {MAKE_PROFILES}")
r|=os.system(f"{CONFIGURE} --host={HOST} --prefix={INSTALL_PREFIX} {PROFILES}")
r|=os.system(f"make {MAKE_PROFILES}")
r|=os.system(f"make install {MAKE_PROFILES}")

sys.exit(0)