# Michelle Scheuer
# CS 432
# 10/13/2021

import os
import time
import subprocess as sp

uri_file = open("files/uniqueURI.txt", "r")
content = uri_file.readlines()
lines = [line.rstrip() for line in content]


for link in lines:
    output = sp.getoutput("echo -n" + link + " | md5 | sed s/$/.html/ | awk '{print $1}'")
    print(output, link)
    # os.popen("curl " + link + " > " + output + " | mv " + output + " files/raw_html_files")

