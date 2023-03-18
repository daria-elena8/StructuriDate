import random

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


v=[ random.randint(0,100) for _ in range(100000) ]
print(*v, '\n')

countS(v)
print(*v, '\n')

