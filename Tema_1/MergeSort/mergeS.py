
import random

def mergeS(lo, hi, v):

    if hi-lo>0:
        mid=(hi-lo)//2 + lo

        mergeS(lo, mid, v)
        mergeS(mid+1, hi, v)

        merge(lo, hi, v)

def merge(lo, hi, v):

    if hi-lo != 0:
        temp=[_ for _ in range(len(v[lo:hi+1]))]
        i=lo
        mid= (hi-lo)//2 + lo
        j=mid+1
        k=0

        while i< mid and j<hi:
            if v[i]<v[j]:
                temp[k]=v[i]
                i+=1
            else:
                temp[k]=v[j]
                j+=1
            k+=1

        while i<mid:
            temp[k]=v[i]
            i+=1
            k+=1

        while j<hi:
            temp[k]=v[j]
            j+=1
            k+=1

        k=0
        for i in range(lo, hi+1):
            v[i]=temp[k]
            k+=1



v=[ random.randint(0,100) for _ in range(15)]
print(*v)

mergeS(0, len(v), v)
print(*v)