# Radix Sort

def redir(temp, v):
	for i in range(len(v)-1):
		for j in range(i-1):
			v[k]=temp[i][j]
			k+=1
	return v

v=[3,2,7,9,1,4]
p=10
ok=1

while(ok):
	ok=0
	
temp=[[] for _ in range(10)]
for i in range(len(v)):
		if v[i]//p!=0:
			ok=1
		temp.append(1)
		
		v=redir(temp, v)
		p*=10

for i in v:
	print(v[i], " ")
