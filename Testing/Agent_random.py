from Utils import *
import time
import socket
import sys
from thread import *

import argparse



parser = argparse.ArgumentParser()


parser.add_argument('-p', '--port', dest="PORT", type=int,
                        default=12121,
                        help='Port')


args=parser.parse_args()


host = '127.0.0.1'
port = args.PORT

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


while 1:
        tm = s.recv(1024)	
        a=str((3.14/2 + 3.14/4) - 0.1)+ ',' + str(1)+','+str(0.49)
	
	try:
		s.send(a)
	except:
		print "Error in sending:",  a
		print "Closing Connection"
		break
s.close()
