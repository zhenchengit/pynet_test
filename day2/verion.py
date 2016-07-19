#!/usr/bin/env python

def show_verion(file):
 with open(file) as f:
   show_ver = f.read().splitlines()
   for line in show_ver:
      if 'Processor board ID' in line:
        _, serial_number = line.split("Processor board ID")
        print "\nSerial Number is {}\n".format(serial_number)
      if 'Cisco IOS Software' in line:
        _, _, ios_version, _ = line.split(",")
        print "\nVersion is {}\n".format(ios_version)

def file_open(file):
 with open(file) as f:
   print f.read()

show_verion('show_version.txt')
#file_open ('show_version.txt')
