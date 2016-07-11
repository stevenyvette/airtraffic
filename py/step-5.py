#coding=utf-8
#统计中国的航空公司各自所有的线路总数


airline = open('cn_route.txt','r')
out = open('cn_route_airline.txt','w')

index=0
a=[]
for line in airline.readlines():
	airtmp=line.split(',')
	tmp=airtmp[0]
	if tmp in a:
		index+=1
	elif len(a):
		out.write(a[-1]+'\t'+str(index)+'\n')
		a.append(tmp)
		index=1
	else:
		a.append(tmp)
		index+=1

out.write(a[-1]+'\t'+str(index)+'\n')

airline.close()
out.close()




