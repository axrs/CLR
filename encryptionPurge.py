import os

baseDir = "/Volumes/"

purgeList = os.curdir + "/encryptionPurge.txt"

if os.path.exists(purgeList):
    lines = []
    # Read the files to be purged
    with open(purgeList) as f:
        lines = f.readlines()
        lines = [line.rstrip('\n') for line in open(purgeList)]

    # Delete each file
    for l in lines:
        fileToPurge = baseDir + l[7:]
        if os.path.exists(fileToPurge):
            print "Removing File: ", fileToPurge
            os.remove(fileToPurge)
