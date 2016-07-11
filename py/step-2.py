#提取中国的航线


airport = open('cn_airport.txt','r')
route = open('route.txt','r')
out = open('cn_route.txt','w')

x=[]

for airline in airport.readlines():
	airtmp=airline.split(',')
	x.append(airtmp[4])

for routeline in route.readlines():
	routetmp= routeline.split(',')
	source='"'+routetmp[2]+'"'
	target='"'+routetmp[4]+'"'
	if (source in x) and (target in x) :
		out.write(routeline)
	

airport.close()
route.close()
out.close()




