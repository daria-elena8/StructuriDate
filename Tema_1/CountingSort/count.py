import random

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




v=[ random.randint(0,100) for _ in range(10) ]
print(*v, '\n')

countingS(v)
print(*v, '\n')

