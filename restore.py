import os
import shutil

baseDir = "/Volumes/restore"

restoreList = os.curdir + "/encryptionPurge.txt"

if os.path.exists(restoreList):
    lines = []
    # Read the files to be purged
    with open(restoreList) as f:
        lines = f.readlines()
        lines = [line.rstrip('\n') for line in open(restoreList)]

    # Delete each file
    for l in lines:
        fileToRestore = baseDir + l[6:-10]
        if not os.path.exists(fileToRestore):
            print "Can't Find File: ", fileToRestore
	else:
	    print "/Volumes" + l[1:-10]
	    shutil.copy2(fileToRestore, "/Volumes/" +  l[1:-10])
