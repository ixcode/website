#!/usr/bin/python
import os
import sys
import time
import datetime

from subprocess import call

environment = sys.argv[1]
ssh_login = os.environ["IXCODE_" + environment + "_SSH"]
ssh_keyfile = os.environ["IXCODE_SSH_KEYFILE"]

print "Going to deploy to [" + environment + "] ..."

call(["ssh", "-i", ssh_keyfile, ssh_login, "ls"])

ts = time.time()

print "[COMPLETED] @ " + datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
