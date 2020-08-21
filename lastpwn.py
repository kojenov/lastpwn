#!/usr/bin/env python3
import hashlib
import sys
import os
import csv
import time

def hibpsearch(csvname, hibpname):

    startTime = time.perf_counter()
    # build a dictionary of password hashes from the CSV
    pwdict = {}
    with open(csvname, newline='') as csvfile:
        pwreader = csv.reader(csvfile)
        for row in pwreader:
            if len(row):
                sha1 = hashlib.sha1(row[2].encode('utf-8')).hexdigest().upper()
                pwdict[sha1] = [row[4], row[1], row[2]]

    # sort the hashes
    myhashes = sorted(pwdict.keys())

    # walk through the HIBP list and find matches
    with open(hibpname) as hibpfile:
        hibphash = hibpfile.readline()[:40]

        # I better not try to explain the logic here
        k = 0
        while hibphash and k < len(myhashes):
            while hibphash and myhashes[k] > hibphash:
                hibphash = hibpfile.readline()[:40]
            if hibphash:
                while k < len(myhashes) and myhashes[k] < hibphash:
                    k = k + 1
                if k < len(myhashes) and myhashes[k] == hibphash:
                    print(pwdict[myhashes[k]])
                    hibphash = hibpfile.readline()[:40]
                    k = k + 1

    endTime = time.perf_counter()
    print(f"Scanned {len(myhashes)} passwords in {endTime - startTime:0.4f} seconds")

# do it!
hibpsearch(sys.argv[1], sys.argv[2])
