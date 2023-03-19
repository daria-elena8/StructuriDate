import time

list1=["date_4.in"]

list2=["Radix4.out"]

timpi=[]

def countS(vec):
    m=max(vec)
    temp=[0 for _ in range(m+1)]
    for i in range(len(vec)):
        temp[vec[i]]+=1

        # am facut temp
    vec.clear()
    for i in range(m+1):
        while temp[i]!=0:
            vec.append(i)
            temp[i]-=1

def radixS(v):
    m=max(v)

    i=1
    while m/i>0:
        countS(v)
        i*=10

for i in range(len(list1)):
    f=open(list1[i], "r")
    g=open(list2[i], "w")
    v=[int(x) for x in f.read().strip().split()]
    
    start=time.time()
    radixS(v)
    end=time.time()
    timpi.append(end-start)
    for j in v:
            g.write(str(j))
            g.write("\n")
    f.close()
    g.close()

g=open("timp_RadixS.out", "w")
for i in timpi:
    g.write(str(i))
    g.write("\n")
g.close()

