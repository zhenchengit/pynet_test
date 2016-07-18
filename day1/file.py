f = (open('file'))
for line in f:
 print line
f.close()

fw = open('new_file','w')
fw.write('dddd\n')
fw.close()
fa = open('new_file','a')
fa.write('eeee\n')
fa.close()
f = (open('new_file'))
for line in f:
 print line
f.close()
