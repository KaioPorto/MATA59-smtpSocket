#!/usr/bin/env python3

import argparse
import socket

#parsing the from, to and msg
parser = argparse.ArgumentParser(description="simple smtp client to send messages"
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-s", "--server", help="mailserver whom gonna receive the message", nargs="*")




def connect((server, port=25)):
    try:
	sock = socket(AF_INET, SOCK_STREAM)
        sock.connect(server, port)
    except:
        print "Unable to connect"

    recv = sock.recv(1024)
    recv = recv.decode()
    if (recv[:3] != '220':
	print("220 reply not received. Not okay.")

#    retrun True

def send_message(msg, _from, to, subject):

    sock.send(b"MAIL FROM" + _from.encode() + "\n")
    #sock.recv("1024")

    sock.send(b"RCPT TO" + to.encode() + "\n")
    #sock.recv("1024")

    sock.send(b"DATA" + bytes(msg, encoding="utf-8") + "\n.\n") 
    #sock.recv("1024")
    
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()

args = parser.parse_args()
server = args.server

mailserver = (server, port)
connect(mailserver)

