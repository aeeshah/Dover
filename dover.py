#!/usr/bin/python

import subprocess
from datetime import datetime
from datetime import date
from fpdf import FPDF
import sys


# Clear the screen
subprocess.call('clear', shell=True)

#variable  pdf
pdf = FPDF()
#addPage
pdf.add_page()
#font and size
pdf.set_font('Times', size = 15)

#pdf_Banner
s = "=" * 60

#Header
pdf.cell(200,10, txt= 'DOVER SCRIPT ', ln = 2, align = 'C')
pdf.cell(200,10, txt= 'Scanning Result of Hosts on your Network', ln = 1, align = 'C')


def bash (command):
	return subprocess.check_output(['bash', '-c', command])

#getting IP
ip_string = bash ('ifconfig eth0 | grep "inet "')
ip = ip_string.strip().split(" ") [1]
print("Your IP address is: " + ip)
pdf.cell(200,10, txt= 'Your IP address is: %s' %ip, ln = 3, align = 'C')

#changing to network
octets = ".".join(ip.split(".")[:- 1])
subnet = octets + ".0/24"

#banner
print("=" * 60)
print("Scanning live hosts on your network: %s" % subnet)
print("=" * 60)


#live Host scan
print("Available live hosts on your network:")
ips = bash('arp-scan %s | cut -d ":" -f1  | grep -E -o "(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)" '  % subnet)

print(ips)
pdf.multi_cell(0, 10,  txt = 'Available live hosts on your network: \n %s' %ips)
ipss = ips.split( )


#nmap for open ports
print("=" * 60)
print("Scanning for open ports on live hosts:")
pdf.cell(0, 10, txt = 'Scanning for open ports on live hosts:' , ln = 6) 
print("=" * 60)


for t in ipss:
	print("TCP Scan report for " + t)
	pdf.cell(0, 10, txt = s , ln = 8)
	pdf.multi_cell(0, 8, txt = 'TCP SCAN REPORT FOR : %s' %t )
	pdf.cell(0, 10, txt = s , ln = 9)
	print("\nPORT   STATE  SERVICE	VERSION")
	pdf.cell(0,8, txt = 'PORT STATE SERVICE VERSION', ln =7)
	liveips = bash('nmap -sS -sV -p- %s | grep "open" ' %t).splitlines()
		
	ports = []
	for port in liveips:
		print(port)
		ports.append(port.split("/")[0])
		pdf.multi_cell(0, 8, txt = port, border = 0)		
		
	pdf.cell(0, 10, txt = s , ln = 10)		
	print("=" * 60)
	#intense Scan
	print("Running an intense Scan on open ports for " +t  )
	pdf.multi_cell(0, 8, txt = 'INTENSE SCAN RESULT FOR : %s' %t )
	pdf.cell(0, 10, txt = s , ln = 11)
	port_list = ",".join(ports)
	intense = bash('nmap -T4 -A -sV -p%s %s' % (port_list, t))
	print(intense)
	print("=" * 60)
	pdf.multi_cell(0, 8, txt = intense, border = 0)
	
#save to file
now = datetime.now()
t1 = now.strftime("%d-%b-%Y %I%M%S")
filename =  "ScanReport_"+ t1	
pdf.output(filename + ".pdf", 'F')


	



