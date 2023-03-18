import random


def merge( lo, mid, hi, v ):
	
	temp=[_ for _ in range(len(v))]

	i=lo
	j=mid+1
	k=0
	while i<mid and j<hi:
		if v[i]<=v[j]:
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
	for i in range(lo, hi+1):
		v[i]=temp[k]
		k+=1


def mergeSort( lo, hi, v ):
	if lo<hi:

		mid=(hi-lo)//2+lo

		mergeSort(lo ,mid,v)
		mergeSort(mid+1, hi, v)

		merge(lo, mid, hi, v)

v=[ random.randint(0,100) for _ in range(20) ]
print(*v)

mergeSort(0,len(v)-1, v)
print(*v)