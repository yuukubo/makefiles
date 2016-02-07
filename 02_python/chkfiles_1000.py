# coding: UTF-8
import datetime
import os
import time
import logging
import random

logging.basicConfig(
    level=logging.DEBUG,
    filename = '1000_chklog.txt',
    format="%(asctime)s %(levelname)s %(module)s %(funcName)s %(lineno)d %(message)s")

i = 0 # loop counter
num = 0 # filename counter
sum_time = 0 # filename counter
TARGET_DIR = "./files/"

while i < 1000 :
    num = random.randint(1,999999)
    TARGET_FILE = "{0:0>6}.txt".format(num)
    start = time.time()
    stat = os.stat(TARGET_DIR + TARGET_FILE)
    last_modified = stat.st_mtime
#    print(last_modified)
    dt = datetime.datetime.fromtimestamp(last_modified)
#    print(dt.strftime("%Y-%m-%d %H:%M:%S"))
    logging.debug(TARGET_FILE + " modified {0}".format(dt.strftime("%Y-%m-%d %H:%M:%S")))
    elapsed_time = time.time() - start
    sum_time += elapsed_time
    i += 1
else:
#    print "ok"
    logging.debug("average elapsed_time:{0} [sec]".format(sum_time / 1000))
