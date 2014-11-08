#!/usr/bin/python
import os, sys, time, datetime

print "Going to deploy to [" + sys.argv[1] + "] ..."

print "Using key [" + os.environ['IXCODE_ENV_KEY'] + "] ..."

ts = time.time()

print "[COMPLETED] @ " + datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
