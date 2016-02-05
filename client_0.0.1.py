# coding: utf-8
import getpass
"""
import socket
s = socket.socket()
s.connect((socket.gethostbyname, 9001))
#!@ check if this is correct address
"""
x = None
while x != "accepted":
	username = raw_input("Username: ")
	password = getpass.getpass("Password: ")
	x = ""
"TESTING GIT UPDATE PUSH"