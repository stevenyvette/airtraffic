#coding=utf-8
#统计中国空港的出度和入度


airline = open('cn_route.txt','r')
out = open('cn_airport_degree.txt','w')

src=0
des=0
out_degree={}
in_degree={}
for line in airline.readlines():
	airtmp=line.split(',')
	src_airport=airtmp[2]
	des_airport=airtmp[4]
	if out_degree.has_key(src_airport):
		out_degree[src_airport]+=1
	else:
		out_degree[src_airport]=1
	if in_degree.has_key(des_airport):
		in_degree[des_airport]+=1
	else:
		in_degree[des_airport]=1
out_degree=sorted(out_degree.iteritems(),key=lambda out_degree:out_degree[1],reverse=True)

for key in out_degree:
	out.write(key[0]+','+str(key[1])+','+str(in_degree.pop(key[0]))+'\n')
airline.close()
out.close()