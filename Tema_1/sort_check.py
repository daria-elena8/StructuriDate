//date_5 - nr intregi (-/+) -50000=>50000
//date_4 - nr naturale nr_7_cifre
//date_3 - nr naturale concentrate in intervalul 157.312-789.253
//date_2 - nr naturale random
//date_1 - nr naturale random <100

import random

f=open('date_5.in', 'a')


v=[ random.randint(-50000,50000) for _ in range(11040) ]

for i in v:
	f.write(str(i))
	f.write("\n")