# nmapexdbsearch

This code will run an Nmap scan with XML output and pass the services running on various ports to the (Exploit-DB) searchsploit program (available from github). The searchsploit program can already do operations of this type with an additional xml library installation, but the XML file from Nmap must already be created. The searches are also either too specific in searchsploit or includes incorrect unparsed service information that ultimately returns missed results.

This code was tested inside Kali Linux and requires the searchsploit program.
