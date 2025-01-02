def blinks(stones, n):
    print(">", n)
    if n == 0:
        return len(stones)

    i = 0
    while i < len(stones):
        s = str(stones[i])
        if stones[i] == 0:
            stones[i] = 1
        elif len(s) % 2 == 0:
            stones[i] = int(s[:len(s)//2])
            stones.insert(i+1, int(s[len(s)//2:]))
            i += 1
        else:
            stones[i] *= 2024
        i += 1
    return blinks(stones, n-1)

# stones = [int(x) for x in open("11test.txt").read().strip().split(" ")]
stones = [int(x) for x in open("11.txt").read().strip().split(" ")]
print(blinks(stones, 25))
