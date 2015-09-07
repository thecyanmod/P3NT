#!/usr/bin/python
# Usage ./Recv.py port

import socket, sys

try:
	print("Recv")
	print("Port:	" + sys.argv[1])
except:
	print("Usage ./Recv.py port")
	sys.exit()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	s.bind(("0.0.0.0", int(sys.argv[1])))
except:
	print("Error while trying to bind to port")
	sys.exit()
s.listen(10)
def recv():
	conn = s.accept()
	data = s.recv(4096)
	if data:
		print(data.decode("utf-8"))
while 1:
	recv()

