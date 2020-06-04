import random
import socket
import struct
from shodan import Shodan
import time
import yaml
import os
from optparse import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

def anim(bcolors):
    print(bcolors.OKBLUE+"_______________"+ bcolors.ENDC)
    print(bcolors.OKBLUE+"< Hello, world! >"+ bcolors.ENDC)
    print(bcolors.OKBLUE+"---------------"+ bcolors.ENDC)
    print(bcolors.OKBLUE+"        \   ^__^"+ bcolors.ENDC)
    print(bcolors.OKBLUE+"         \  (oo)\_______"+ bcolors.ENDC)
    print(bcolors.OKBLUE+"            (__)\       )/\/"+ bcolors.ENDC)
    print(bcolors.OKBLUE+"                ||----w |"+ bcolors.ENDC)
    print(bcolors.OKBLUE+"                ||     ||   https://github.com/Rikozi/ipportcheck.py"+ bcolors.ENDC)
anim(bcolors)
parser = OptionParser( """
Usage: python3 ipportcheck.py [options]
options:
-p / --port :: Port that do you want to get
ex:
   script.py -p 80
   script.py -port 80

""")
parser.add_option("-p","--port",type="string",dest="port",help="Port that do you want to get")
(options,args) = parser.parse_args()
if options.port == None:
    print(parser.usage)
    exit(0)
else:
    port = (options.port)

os.system('clear')
for i in range(100000):
    ip = ".".join(map(str, (random.randint(0, 255) 
                           for _ in range(4))))

    response = os.popen("ping -c1 -W1 " + ip).read()
    
    if "icmp_seq=1" in response:
        retry = 2
        delay = 1
        timeout = 1
        #print("[+] UP " + ip +" Ping Successful").format()       
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
            s.connect((ip, int(port)))
            s.shutdown(socket.SHUT_RDWR)
            rojola = True
        except:
            rojola = False
        finally:
            s.close()
        ipup = False
        for i in range(retry):
            if rojola == True:
                ipup = True
                break
            else:
                time.sleep(delay)
        
        if ipup == True:
            print (bcolors.OKGREEN+ "Discovered open port " + str(port) + " on "+ ip + bcolors.ENDC)
        else:
            print(bcolors.WARNING+"port " + str(port) + " on " + ip + " is down"+bcolors.ENDC)

        if ipup == True :
            SHODAN_API_KEY = "RsA1mYGuorNloKbrWsaZT8NoRg6siYWH"
            api = Shodan(SHODAN_API_KEY)
            try:
                response = api.host(ip)
            except shodan.exception.APIError as e:
                raise Exception('Shodan: {}'.format(e))
            data = response['data']
            data_list = []
            for item in data:
                data_list.append(item['data'])
                dict = {
            'ip_str': response.get('ip_str'),
            'country_name': response.get('country_name'),
            'country_code': response.get('country_code'),
            'os': response.get('os'),
            'ports': response.get('ports')
          
            }
            print (yaml.dump(dict))
            
        
