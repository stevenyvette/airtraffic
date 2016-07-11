f=open('../document/cn_airport_degree2.txt','r')
out=open('../document/cn_airport_location.txt','w')


for line in f.readlines():
	tmp=line.split(',')
	print tmp
	out.write("'"+tmp[0]+"':["+tmp[4]+","+tmp[5][:-3]+"],\n")

f.close()
out.close()
