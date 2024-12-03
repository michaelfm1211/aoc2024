from re import findall

with open("3.txt") as f:
    data = f.read()

insts = findall(r"(?:mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))", data)
s = 0
on = True
for x, y, do, dont in insts:
    if do != "":
        on = True
        continue
    if dont != "":
        on = False
        continue
    if not on:
        continue
    s += int(x) * int(y)
print(s)
