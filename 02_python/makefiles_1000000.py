# coding: UTF-8
import time
import logging
import os

TARGET_DIR = "./files"
i = 0 # loop counter

logging.basicConfig(
	level=logging.DEBUG,
	filename = '100000_makelog.txt',
	format="%(asctime)s %(levelname)s %(module)s %(funcName)s %(lineno)d %(message)s")

logging.debug(" **** start **** ")

if not os.path.isdir(TARGET_DIR):
	os.makedirs(TARGET_DIR)

start = time.time()

while i < 1000000 :
#	start = time.time()
	f = open(TARGET_DIR + "/{0:0>6}.txt".format(i), "w")
	f.write("")
	f.close()
#	elapsed_time = time.time() - start
#	logging.debug("elapsed_time:{0}".format(elapsed_time))
	i += 1
else:
#	print "ok"
	elapsed_time = time.time() - start
	logging.debug("elapsed_time:{0} [sec]".format(elapsed_time))

logging.debug(" **** end **** ")
