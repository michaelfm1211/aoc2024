diskmap = open("9.txt").read().strip()

fs = []
file = True
for i in range(len(diskmap)):
    flen = int(diskmap[i])
    if file:
        fs += [str(i//2)]*flen
    else:
        fs += ['.']*flen
    file = not file
# print("".join(fs))

endptr = len(fs)-1
while fs[endptr] == '.':
    endptr -= 1

i = 0
while endptr > i:
    if fs[i] == '.':
        fs[i] = fs[endptr]
        fs[endptr] = '.'
        while fs[endptr] == '.':
            endptr -= 1
    i += 1
# print("".join(fs))

chksum = 0
i = 0
while fs[i] != '.':
    chksum += i*int(fs[i])
    i += 1
print(chksum)
