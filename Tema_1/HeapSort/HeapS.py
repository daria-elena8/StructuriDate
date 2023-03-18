import random

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



v=[ random.randint(0,100) for _ in range(15)]
print(*v)

heapS(v, len(v))
print(*v)