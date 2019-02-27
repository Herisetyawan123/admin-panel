import requests
import os



banner = '\033[94;1m'+'''                    @             |
 _____  ___         _ _  ___      |
/     \|   \|\    /| | |/__ |     |
|  _  ||   || \  / | |  /  ||     |
|_| |_||___/|_|\/|_|_|_|   ||	  |
				  |
__________________________________|

\033[91;1mTeam : famousXploitTeam()

Usage :
	- python2 admin.py
'''
def check(url):
	name_file = raw_input('nama file : ')
	with open('list.txt', 'r') as r:
		data = r.read()
	admin = data.split()
	
	for admins in admin:
			
		req=requests.get(url+"/"+admins)
		if req.status_code == 200:
			url_file = url+"/"+admins+"\n"
			print '\033[97;1m'+url+'/'+admins+'\033[96;1m => Success'
			file_hasil = open(name_file, 'a')
			file_hasil.write(url_file)
			file_hasil.close()
		else:
			print '\033[97;1m'+url+'/'+admins+'\033[91;1m => not found'
	
def execute():
	os.system('clear')
	print banner
	url = raw_input('\033[92;1mEnter your target : ')
	if not url.startswith('http'):
		url = 'http://'+url
	check(url)
try:
	execute()
except requests.ConnectionError, e:
	print '\033[91;1m[*] your computer not connect to internet'
