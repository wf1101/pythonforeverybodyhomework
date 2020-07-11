# print('Hello folks! I am very existed to be taking Python For Everyone course!')
# print('My goal is to learn Python and use Python for technical interviews.')

# tra = input("who are you?")
# print('welcome',tra)

# inp = input('Europen floor?')
# usf = int(inp) + 1
# print('US floor', usf)

# hour = input("Enter Hours: ")
# rate = input("Enter rate: ")
# try:
#     fh = float(hour)
#     fr = float(rate)
# except:
#     print("Error! Please input numeric values.")
#     quit()
#
# if fh > 40 :
#     print(40 * fr + (fh - 40) * 1.5 * fr)
# else :
#     print(fh * fr)

# while True :
#     line = input('> ')
#     if line == 'done' :
#         break
#     elif line == 'hello':
#         continue
#     print(line)

# str = "dada-da-da-232-da: 0.8475"
# ipos = str.find('0')
# print(ipos)
# val = float(str[ipos:len(str)])
# print(val)

# import re
#
# fileName = "data.txt"
# fileHanle = open(fileName)
# res = 0
# for ln in fileHanle:
#     nums = re.findall('[0-9]+', ln)
#     for num in nums:
#         res = res + int(num)
# print(res)

# import socket
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')
#
# mysock.close()
#
# import urllib.request
#
# fhand = urllib.request.urlopen("http://data.pr4e.org/intro-short.txt")
#
# for line in fhand:
#     print(line.decode().strip())

# import urllib.request
# from bs4 import BeautifulSoup
# import ssl
#
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_node = ssl.CERT_NONE
#
# url = input("Enter - ")
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
#
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter - ')
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")
#
# # Retrieve all of the anchor tags
# tags = soup('span')
# res = 0
# for tag in tags:
#     res = res + int(tag.contents[0])
# print(res)

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
#
# # Retrieve all of the anchor tags
# tags = soup('a')
# cnt = 0
# for tag in tags:
#     cnt = cnt + 1
#     if cnt == 18:
#         print(tag.get('href', None))
#         url = tag.get('href', None)
#
# for idx in range(6):
#     html = urllib.request.urlopen(url, context=ctx).read()
#     soup = BeautifulSoup(html, 'html.parser')
#     tags = soup('a')
#     cnt = 0
#     for tag in tags:
#         cnt = cnt + 1
#         if cnt == 18:
#             print(tag.get('href', None))
#             url = tag.get('href', None)

# import xml.etree.ElementTree as ET
#
# data = '''
# <users>
#     <person>
#       <name>Tracy</name>
#       <phone type="intl">
#         + 1 7324
#       </phone>
#     </person>
#     <person>
#       <name>Alex</name>
#       <phone type="intl">
#         + 1 7777
#       </phone>
#     </person>
# </users>'''
#
# tree = ET.fromstring(data)
# lst = tree.findall('person')
# for item in lst:
#     print("Name", item.find('name').text)
#     print("Attr", item.find('phone').get('type'))

# import urllib.request, urllib.parse, urllib.error
# import xml.etree.ElementTree as ET
# import ssl
#
# url = 'http://py4e-data.dr-chuck.net/comments_777622.xml'
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# print('Retrieving', url)
# uh = urllib.request.urlopen(url, context=ctx)
#
# data = uh.read()
# print('Retrieved', len(data), 'characters')
# print(data.decode())
# tree = ET.fromstring(data)
#
# res = 0
# results = tree.findall('.//count')
# for cnt in results:
#     res = res + int(cnt.text)
# print(res)

# import urllib.request, urllib.parse, urllib.error
# import json
#
# gepurl = 'maps.googleapis.com/maps/api/geocode/json?'
#
# address = input("Enter Localtion: ")
# # if len(address) < 1: break
#
# url = gepurl + urllib.parse.urlencode(
#     {'address': address})
# print("Retrieving", url)
#
# uh = urllib.request.urlopen(url)
# data = uh.read().decode()
# print("Retrieved", len(data), 'charavters')
#
# try:
#     js = json.load(data)
# except:
#     js = None
#
# if not js or 'status' not in js or js['status'] != 'OK':
#     print("===Failure To Retrieve Data===")
#     print(data)
# print(json.dumps(js, indent=4))
#
# lat = js["results"][0]["geometry"]["location"]["lat"]
# lng = js["results"][0]["geometry"]["location"]["lng"]
# print("lat", lat, "lng", lng)
# locaton = js["results"][0]["formatted_address"]
# print(location)

# import urllib.request, urllib.parse, urllib.error
# import json
#
# url = 'http://py4e-data.dr-chuck.net/comments_777623.json'
# data = urllib.request.urlopen(url).read()
#
# info = json.loads(data)
# print(info)
#
# res = 0
#
# for com in info["comments"]:
#     res = res + int(com["count"])
# print(res)

import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    print("Place id", js["results"][0]["place_id"])


    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        continue

    # print(json.dumps(js, indent=4))
