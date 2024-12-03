from re import findall

with open("3.txt") as f:
    data = f.read()

insts = findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
s = 0
for inst in insts:
    s += int(inst[0]) * int(inst[1])
print(s)
