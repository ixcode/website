#!/usr/bin/python
import sys, time, datetime

print "Going to deploy to [" + sys.argv[1] + "] ..."

ts = time.time()

print "[COMPLETED] @ " + datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
