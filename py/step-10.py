f=open("../document/degree-betweennesscentrality.txt",'r')
out=open("../document/degree_betweenness_final.txt",'w')

for line in f.readlines():
	tmp=line.split(',')
	out.write("["+tmp[2]+","+tmp[4][:-1]+",'"+tmp[1]+"'],\n")

f.close()
out.close()
