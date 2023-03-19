import time

list1=["date_1.in", "date_2.in", "date_3.in", "date_4.in", "date_5.in"]

list2=["Shell1.out", "Shell2.out", "Shell3.out", "Shell4.out", "Shell5.out"]

timpi=[]

def shellS(v, n):
    gap=n//2
    while gap>0:
        j=gap
        while j<n:

            i=j-gap

            while i>=0:
                if v[gap+i]<=v[i]:
                    v[gap+i],v[i]=v[i],v[gap+i]
                else:
                    break
                i-=gap
            j+=1
        gap//=2

for i in range(len(list1)):
    f=open(list1[i], "r")
    g=open(list2[i], "w")
    v=[int(x) for x in f.read().strip().split()]
    
    start=time.time()
    shellS(v, len(v)-1)
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

