#!/usr/bin/python

import os
from subprocess import call

print "Working in : " + os.getcwd()

call(["pip", "install", "virtualenv"])

venv_path = os.getcwd() + "/lib/venv"

if not os.path.exists(os.getcwd() + "/lib/venv"):
    os.makedirs(venv_path)

call(["virtualenv", venv_path])


