import os

baseDir = "/Volumes/BACKUPS/rsnapshot/hourly.4/fs/Volumes"

restoreList = os.curdir + "/encryptionPurge.txt"

if os.path.exists(restoreList):
    lines = []
    # Read the files to be purged
    with open(restoreList) as f:
        lines = f.readlines()
        lines = [line.rstrip('\n') for line in open(restoreList)]

    # Delete each file
    for l in lines:
        fileToRestore = baseDir + l[1:]
        if os.path.exists(fileToRestore):
            print "Restore File: ", fileToRestore
        else:
            print "Can't Find File: ", fileToRestore
