from collections import Counter

lst1 = []
lst2 = []
for line in open("1test.txt"):
    id1, id2 = (int(x) for x in line.split("   "))
    lst1.append(id1)
    lst2.append(id2)

c = Counter(lst2)
score = 0
for loc in lst1:
    score += loc * c[loc]
print(score)
