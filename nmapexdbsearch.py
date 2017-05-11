#!/usr/bin/env python
import sys
import subprocess
import xml.etree.ElementTree as ET

def acquire_input_and_run_nmap():
	host = input("What is the hostname or IP address?  ")
	ports = input("What port(s) do you want to scan? ex. 80 or 1-65535  ")
	command = ("nmap -oX - -A -Pn %s -p %s" % (host, ports))
	p = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
	root = ET.fromstring(p.stdout)
	return root

def process_nmap_port_services(root):
	info = []
	for service in root.iter('service'):
		output = service.get('product')
		info.append(output)
	return info

def clean_output(info):
	info = [x for x in info if x != None] # Takes out None types
	print("\nThese services have been found %s\n" % info)
	info = ([s.strip('httpd') for s in info]) # Takes out httpd because it limits search results
	return info

def searchsploit_search(cleanservices):
	for cleanservices in cleanservices:
		print("\nSEARCHING FOR THE %s SERVICE\n" % cleanservices)
		command = ("searchsploit %s" % cleanservices)
		subprocess.run(command, shell=True)
		
def main():
	print("\nMake sure the searchsploit program is up-to-date. i.e. searchsploit -u \n")
	root = acquire_input_and_run_nmap()
	services = process_nmap_port_services(root)
	cleanservices = clean_output(services)
	searchsploit_search(cleanservices)
	
if __name__ == "__main__":
	main()
