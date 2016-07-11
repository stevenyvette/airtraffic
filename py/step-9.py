f=open('../document/cn_airport_link.txt','r')
out=open('../document/cn_airport_link_format.txt','w')

for line in f.readlines():
	try:
		tmp=line.split(',')
		out.write("[{name:'"+tmp[0]+"'},{name:'"+tmp[1]+"',value:"+tmp[2][:-1]+"}],\n")
		print tmp
	except:
		print line

f.close()
out.close()