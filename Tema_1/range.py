
list1=["date_1.in", "date_2.in", "date_3.in", "date_4.in", "date_5.in"]

for i in range(len(list1)):
    f=open(list1[i], "r")
    v=[int(x) for x in f.read().strip().split()]
    mic=min(v)
    mare=max(v)
    print(f"setul {i+1}: {len(v)} numere;               minimul: {mic}                      maximul: {mare} ")