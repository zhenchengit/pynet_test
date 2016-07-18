#!phthon 2
ip = raw_input("please type ip :")
# print "{:<12} {:<12} {:<12} {:<12}".format(*ip.split('.'))
ip_addr = ip.split(".")
ip_addr[3]='0'
print (ip_addr[0],ip_addr[1],ip_addr[2],ip_addr[3])
print (bin(int(ip_addr[0])),bin(int(ip_addr[1])),bin(int(ip_addr[2])),bin(int(ip_addr[3])))
