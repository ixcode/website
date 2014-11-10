#!/usr/bin/python

import os.path
from subprocess import call


def ensure_dir(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)


# ensure_dir("target")


call(["cd", "target"])
call(["git"])