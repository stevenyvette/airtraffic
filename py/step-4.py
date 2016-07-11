#coding=utf-8
#统计中国的航空公司


airline = open('cn_airlines.txt','r')
out = open('cn_airlines_simple.txt','w')


for line in airline.readlines():
	airtmp=line.split(',')
	res=airtmp[3]+'\t'+airtmp[1]+'\n'
	out.write(res)
	

airline.close()
out.close()




