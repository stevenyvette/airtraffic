f=open('cn_airport_link.txt','r')
tmp=0
for line in f.readlines():
	if line.split(',')[0]=="NKG" or line.split(',')[1]=="NKG":
		tmp+=1
		print line
print tmp

f.close()