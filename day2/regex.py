#!/usr/bin/env python
import re
re.compile('<title>(.*)</title>')

def show_verion(file):
 with open(file) as f:
   show_ver = f.read().splitlines()
   for line in show_ver:
    match_version = re.search("Cisco IOS Software, .*, Version (.*), RELEASE", line, flags=re.MULTILINE)
    if match_version:
      print match_version.group(1)   
    match_ser = re.search("^Processor board ID (.*)", line, flags=re.MULTILINE)
    if match_ser:
      print match_ser.group(1)
    match_up = re.search("uptime is (.*)", line, flags=re.MULTILINE)
    if match_up:
      print match_up.group(1)


show_verion('show_version.txt')
