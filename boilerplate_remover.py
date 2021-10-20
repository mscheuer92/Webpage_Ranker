# Michelle Scheuer
# CS 432
# 10/13/2021

import time
from boilerpy3 import extractors
import os
import codecs

extractor = extractors.ArticleExtractor()

for a in os.listdir("files/raw_html_files"):
    # lines 70-74 borrowed from https://stackoverflow.com/questions/3269293/how-to-write-a-check-in-python-to-see-if-file-is-valid-utf-8
    try:
        f = codecs.open("files/raw_html_files/" + a, encoding='utf-8', errors='ignore')
        for line in f:
            pass
    except UnicodeDecodeError:
        os.popen("mv files/raw_html_files/" + a + " files/processed_no_useful_text | rm  files/raw_html_files/" + a)

    filesize = os.path.getsize("files/raw_html_files/" + a)
    if filesize == 0:
        os.popen("mv files/raw_html_files/" + a + " files/processed_no_useful_text | rm  files/raw_html_files/" + a)
        time.sleep(2)
    else:
        content = extractor.get_content_from_file("files/raw_html_files/" + a)
        os.popen("touch " + a + "| rm  files/raw_html_files/" + a)
        file = open(a, "w")
        file.write(content)
        file.close()

        file = open(a, "r")
        file.readlines()
        filesize = os.path.getsize(a)
        os.popen("mv " + a + " files/processed_html_files")
