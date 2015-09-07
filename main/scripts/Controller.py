#!/usr/bin/python
# P3NT Controller

import Send, Recv

print("[P3NT]Python3 Network Tools")
while 1:
	com = input("[P3NT]Enter command: ")
	if com == "help":
		print("[P3NT]Commands:")
		print("[P3NT]    send Sends Messages")
		print("[P3NT]    recv Listens for Messages")
		print("[P3NT]More Information on the P3NT GitHub wiki")
	elif com == "send":
		Send.send()
	elif com == "recv":
		Recv.recv()

