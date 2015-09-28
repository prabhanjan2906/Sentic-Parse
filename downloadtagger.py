#! /usr/lib/env python

import urllib2
import os, zipfile
import shutil

url =  "http://nlp.stanford.edu/software/stanford-postagger-2014-01-04.zip"



file_name = url.split('/')[-1]
u = urllib2.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
print meta
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    #print status,

f.close()

zip_file = "stanford-postagger-2013-04-04.zip"


with zipfile.ZipFile(zip_file, "r") as z:
    z.extractall( )

shutil.move("stanford-postagger-2013-04-04", "stanford-postagger")