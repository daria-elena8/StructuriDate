import time

list1=["date_1.in", "date_2.in", "date_3.in", "date_4.in", "date_5.in"]

list2=["Merge1.out", "Merge2.out", "Merge3.out", "Merge4.out", "Merge5.out"]

timpi=[]

def mergeS(lo, hi, v):

    if hi-lo>0:
        mid=(hi-lo)//2 + lo

        mergeS(lo, mid, v)
        mergeS(mid+1, hi, v)

        merge(lo, hi, v)

def merge(lo, hi, v):

    if hi-lo != 0:
        
        temp= [ _ for _ in range(len(v[lo:(hi+1)]))]
        i=lo
        mid= (hi-lo)//2 + lo
        j=mid+1
        k=0



        while i<= mid and j<=hi:
            if v[i]<v[j]:
                temp[k]=v[i]
                i+=1
            else:
                temp[k]=v[j]
                j+=1
            k+=1

        while i<=mid:
            temp[k]=v[i]
            i+=1
            k+=1

        while j<=hi:
            temp[k]=v[j]
            j+=1
            k+=1
        

        k=0
        i=lo
        while i<=hi:
            v[i]=temp[k]
            i+=1
            k+=1
        


for i in range(len(list1)):
    f=open(list1[i], "r")
    g=open(list2[i], "w")
    v=[int(x) for x in f.read().strip().split()]
    
    start=time.time()
    mergeS(0, len(v)-1, v)
    end=time.time()
    timpi.append(end-start)
    for j in v:
            g.write(str(j))
            g.write("\n")
    f.close()
    g.close()

g=open("timp_mergeS.out", "w")
for i in timpi:
    g.write(str(i))
    g.write("\n")
g.close()

