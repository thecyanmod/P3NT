#!/usr/bin/python
# Usage ./Send.py [host] [port] [message] [count]

import socket, sys

try:
	print("[S]>Send")
	print("[S]>Host:		" + sys.argv[1])
	print("[S]>Port:		" + sys.argv[2])
	print("[S]>Message:	" + sys.argv[3])
	print("[S]>Count:		" + sys.argv[4])
except:
	print("[S]>Usage: ./Send.py [host] [port] [message] [count]")
	sys.exit()
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
	print("[S]>Error while trying to create socket")
	sys.exit()
try:
	s.connect((sys.argv[1], int(sys.argv[2])))
except:
	print("[S]>Error while trying to connect")
	sys.exit()
def send():
	try:
		s.send(bytes(sys.argv[3], "utf-8"))
	except:
		print("[S]>Error while trying to send message")
	except KeyboardInterrupt:
		print("[S]>Program terminated")
		sys.exit()
for i in range(1, int(sys.argv[4])):
	send()
try:
	s.close()
except:
	print("[S]>Error while trying to close socket")

