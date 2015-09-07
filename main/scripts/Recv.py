#!/usr/bin/python
# P3NT Recv

import socket, sys

def recv():
	try:
		print("[P3NT]Recv")
		p = input("[P3NT]Port: ")
	except KeyboardInterrupt:
		print("[P3NT]Program terminated")
		sys.exit()
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.bind(("0.0.0.0", int(p)))
	except:
		print("[P3NT]Error while trying to bind to port")
		sys.exit()
	s.listen(10)
	def recv():
		conn = s.accept()
		data = s.recv(4096)
		if data:
			print(data.decode("utf-8"))
	while 1:
		recv()

