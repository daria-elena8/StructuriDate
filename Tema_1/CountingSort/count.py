import time

list1=["date_1.in", "date_2.in", "date_3.in", "date_4.in", "date_5.in"]

list2=["Count1.out", "Count2.out", "Count3.out", "Count4.out", "Count5.out"]

timpi=[]

def countingS(vec):
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


for i in range(len(list1)):
    f=open(list1[i], "r")
    g=open(list2[i], "w")
    v=[int(x) for x in f.read().strip().split()]
    if min(v)<0:
        g.write("nu se poate realiza sortarea")
        timpi.append(0)

    else:
        start=time.time()
        countingS(v)
        end=time.time()
        timpi.append(end-start)
        for j in v:
            g.write(str(j))
            g.write("\n")
        f.close()
        g.close()

g=open("timp_count.out", "w")
for i in timpi:
    g.write(str(i))
    g.write("\n")
g.close()

