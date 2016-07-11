#提取中国的航空公司

airline = open('airlines.txt','r')
out = open('cn_airlines.txt','w')


for line in airline.readlines():
	airtmp=line.split(',')
	if airtmp[6]=='"China"':
		out.write(line)
	

airline.close()
out.close()




