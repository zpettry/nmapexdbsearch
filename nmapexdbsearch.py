#!/usr/bin/env python
import sys
import subprocess
import xml.etree.ElementTree as ET

def acquire_input_and_run_nmap():
	host = sys.argv[1]
	command = ("nmap -oX - -A -p 1-65535 -Pn %s" % host)
	p = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
	root = ET.fromstring(p.stdout)
	return root

def get_nmap_port_services(root):
	info = []
	for service in root.iter('service'):
		output = service.get('product')
		info.append(output)
	return info

def searchsploit_search(cleanservices):
	for cleanservices in cleanservices:
		command = ("searchsploit %s" % cleanservices)
		subprocess.run(command, shell=True)
		
def main():
	root = acquire_input_and_run_nmap()
	services = get_nmap_port_services(root)
	cleanservices = [x for x in services if x != None]
	searchsploit_search(cleanservices)
	
if __name__ == "__main__":
	main()