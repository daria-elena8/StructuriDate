import time

list1=["date_1.in", "date_2.in", "date_3.in", "date_4.in", "date_5.in"]

list2=["Heap1.out", "Heap2.out", "Heap3.out", "Heap4.out", "Heap5.out"]

timpi=[]

def heapify( v, i, n ):
    root=i

    stg=2*i+1
    dr=2*i+2


    if stg<n and v[stg]<v[root]:
        root=stg

    if dr<n and v[dr]<v[root]:
        root=dr

    if root != i:
        v[i],v[root]=v[root],v[i]
        heapify(v, root, n)



def heapS(v, n):
    for i in range(n//2-1, -1, -1):
        heapify(v, i, n)

    for i in range(n-1, 0, -1):
        v[i], v[0]=v[0], v[i]

        n=i
        heapify(v, 0, n)
    v.reverse()


for i in range(len(list1)):
    f=open(list1[i], "r")
    g=open(list2[i], "w")
    v=[int(x) for x in f.read().strip().split()]
    
    start=time.time()
    heapS(v, len(v)-1)
    end=time.time()
    timpi.append(end-start)
    for j in range(1,len(v)-1):
            g.write(str(v[j]))
            g.write("\n")
    f.close()
    g.close()

g=open("timp_heap.out", "w")
for i in timpi:
    g.write(str(i))
    g.write("\n")
g.close()

