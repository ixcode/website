#!/usr/bin/python
import os, sys, time, datetime
from subprocess import call

environment = sys.argv[1]
ssh_login = os.environ["IXCODE_SSH_" + environment]

print "Going to deploy to [" + environment + "] ..."

print "Using key [" + os.environ['IXCODE_ENV_KEY'] + "] ..."

call(["ssh", "-v", ssh_login, "ls"])

ts = time.time()

print "[COMPLETED] @ " + datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
