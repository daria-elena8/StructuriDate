

import random

f=open('date_2.in', 'a')


v=[ random.randint(0,5000000) for _ in range(1104000) ]

for i in v:
	f.write(str(i))
	f.write("\n")