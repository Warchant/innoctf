#!/usr/bin/python2
import multiprocessing as mp
import logging
import socket
import time
import hashlib
import random
import string

logger = mp.log_to_stderr(logging.DEBUG)


def level(i, client, address):
	alphabet = string.lowercase + "1234"
	s = "".join([random.choice(alphabet) for x in range(21)]) 

	Q = random.randint(0, len(hashlib.algorithms)-1)
	chash = lambda x: getattr(hashlib, hashlib.algorithms[Q])(x).hexdigest()
	h = chash(s)

	client.send("\nLevel "+str(1+i)+"/5. To continue you must provide proof of work: \nSend us a string starting with "+ s[:16] +", ^[1-4a-z]{21}$, such that its "+ str(hashlib.algorithms[Q]) +" sum equals to "+h+".\n")
	
	# receive answer
	answer = client.recv(23) # 21 + \r\n
	if chash(answer[:21]) == h:
		client.send("correct!\n")
		logger.debug("{0} passed {1} level. ".format(address, i+1))
		return True
	else:
		client.send("wrong\n")
		client.close()


def worker(socket):
	global FLAG

	while True:
		try:
			client, address = socket.accept()

			logger.debug("{0} connected. ".format(address))

			for i in range(5):
				level(i, client, address)
			client.send("You're bruteforce master! your flag: " + str(FLAG))

			client.close()
		except Exception as e:
			logger.debug("{0} disconnected. ".format(address))
			print(e)


if __name__ == '__main__':
	global FLAG
	global PORT

	PORT = 50001
	with open("flag.txt", "rb") as r:
		FLAG = r.read()

	cpus = mp.cpu_count()
	num_workers = cpus if cpus > 1 else 4

	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	serversocket.bind(('',PORT))
	serversocket.listen(5)

	workers = [mp.Process(target=worker, args=(serversocket,)) for i in
			range(num_workers)]

	for p in workers:
		p.daemon = True
		p.start()

	while True:
		try:
			time.sleep(10)
		except:
			break