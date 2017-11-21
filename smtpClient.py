#!/usr/bin/env python3

import argparse
import socket

#parsing the from, to and msg

def connect(server, port=25):
    try:
        sock = socket.create_connection((server, port))
    except:
        print "Unable to connect"

def send_message(msg, _from, to, subject):

    sock.send(b"MAIL FROM" + _from.encode() + "\n")
    #sock.recv("1024")

    sock.send(b"RCPT TO" + to.encode() + "\n")
    #sock.recv("1024")

    sock.send(b"DATA" + bytes(msg, encoding="utf-8") + "\n.\n") 
    #sock.recv("1024")
    
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()


