#coding=utf-8
#统计中国空港的连边 (无向)


airline = open('cn_route.txt','r')
out = open('cn_airport_link.txt','w')

dic={}
for line in airline.readlines():
	airtmp=line.split(',')
	src_airport=airtmp[2]
	des_airport=airtmp[4]
	key=src_airport+','+des_airport
	reverse=des_airport+','+src_airport
	if dic.has_key(key):
		dic[key]+=1
	elif dic.has_key(reverse):
		dic[reverse]+=1
	else:
		dic[key]=1

dic=sorted(dic.iteritems(),key=lambda dic:dic[1],reverse=True)

for key in dic:
	out.write(key[0]+','+str((key[1]+1)/2)+'\n')

airline.close()
out.close()