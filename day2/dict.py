#!/usr/bin/env python

dict={'router': '10.1.1.1 admin admin123 cisco 4900', 'firewall': '10.1.1.2 admin admin123 juniper 2900', 'switch': '10.1.1.3 admin admin123 arist 7500' }

print dict

for item in dict:
 temp=dict[item].split()
 temp[2] = "123admin"
 temp.append("secret")
 dict[item] = temp
 
print dict

print dict.get('abc','cisco_ios')

try:
 dict['router']
