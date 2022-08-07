# try getting banner from open ports

import socket # in order to communicate with other devices
import termcolor # colors output differently
import subprocess # sends commands out into the terminal
try:
	from subprocess import DEVNULL
except ImportError:
	import os
	DEVNULL = open(os.devnull, 'wb')

pings = 1

def scan(target, ports):
	if received == -1:
		pass
	elif received == 0:
		pass
	else:
		print(termcolor.colored('[+] Host Discovered at: ' + str(target), 'green'))
		print(termcolor.colored(('[*] Targeting Discovered Host: ' + str(target.strip(' '))), 'green'))
		for port in range(1,ports+1):
			port_scanner(target,port)



def port_scanner(ipaddr, port):
	try:
		sock = socket.socket()
		sock.connect((ipaddr, port))
		print(termcolor.colored(('[+] Port Opened '+ str(port)), 'blue'))
		sock.close()
	except:
		pass



def ping(target):
	try:
		command = ['ping', '-c', str(pings),'-q',  target]
	except:
		pass
		
	return subprocess.run(command, stdout=subprocess.PIPE, stderr=DEVNULL)






targets = input('[*] Enter A Targets To Scan (split by \',\'): \n')
ports = int(input('[*] Enter How Many Ports You Want To Scan: \n'))
if ',' in targets:
	print(termcolor.colored(('[*] Scanning Multiple Targets!'), 'red'))
	for ipaddr in targets.split(','):
		state = str(ping(ipaddr.strip(' ')))
		received = state.find('returncode=0')
		scan(ipaddr.strip(' '),ports)
else:
	print(termcolor.colored(('[*] Scanning Single Target!'), 'red'))
	state = str(ping(targets.strip(' ')))
	received = state.find('returncode=0')
	scan(targets.strip(' '),ports)











