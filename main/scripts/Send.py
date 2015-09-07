#!/usr/bin/python
# P3NT Send

import socket, sys

def send():
	try:
		print("[P3NT]Send")
		h = input("[P3NT]Host: ")
		p = input("[P3NT]Port: ")
		m = input("[P3NT]Message: ")
		c = input("[P3NT]Count: ")
	except KeyboardInterrupt:
		print("[P3NT]Program terminated")
		sys.exit()
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except:
		print("[P3NT]Error while trying to create socket")
		sys.exit()
	try:
		s.connect((h, int(p)))
	except:
		print("[P3NT]Error while trying to connect")
		sys.exit()
	def send():
		try:
			s.send(bytes(m, "utf-8"))
		except:
			print("[P3NT]Error while trying to send message")
			sys.exit()
	for i in range(1, int(c)):
		send()
	try:
		s.close()
	except:
		print("[P3NT]Error while trying to close socket")

