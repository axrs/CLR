#!/usr/bin/python

import os
import time

print "User number",  os.getuid()
print "Process ID", os.getpid()
print "Current Directory", os.getcwd()
print "System information", os.uname()
print "System information", os.times()

print "Time is now", time.time()