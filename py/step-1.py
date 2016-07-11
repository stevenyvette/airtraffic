#提取中国的机场


f = open('airport.txt','r')
out = open('cn_airport.txt','w')

for line in f.readlines():
	try:
		tmp= line.split(',')
		if(tmp[3]=='"China"'):
			out.write(line)
	except:
		print line

f.close()
out.close()




