lst1 = []
lst2 = []
for line in open("1.txt"):
    id1, id2 = (int(x) for x in line.split("   "))
    lst1.append(id1)
    lst2.append(id2)

lst1.sort()
lst2.sort()
total_dist = sum(abs(x - y) for x, y in zip(lst1, lst2))
print(total_dist)
