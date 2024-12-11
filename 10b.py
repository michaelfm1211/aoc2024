def get_adj(grid, pos):
    i, j = pos
    adjs = []
    if i > 0:
        adjs.append((i-1, j))
    if i < len(grid) - 1:
        adjs.append((i+1, j))
    if j > 0:
        adjs.append((i, j-1))
    if j < len(grid[0]) - 1:
        adjs.append((i, j+1))
    return [(ai, aj) for ai, aj in adjs if grid[ai][aj] == grid[i][j] + 1]

grid = [[int(x) if x != '.' else -1 for x in line.strip()] for line in open("10.txt")]

heads = []
for i, line in enumerate(grid):
    for j, height in enumerate(line):
        if height == 0:
            heads.append((i, j))

sum_ratings = 0
for head in heads:
    def seen(pos):
        if grid[pos[0]][pos[1]] == 9:
            return 1
        return sum(seen(adj) for adj in get_adj(grid, pos))
    sum_ratings += seen(head)
print(sum_ratings)
