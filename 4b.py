grid = [line.strip() for line in open("4.txt")]
cnt = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != "A":
            continue
        if i == 0 or i == len(grid)-1 or j == 0 or j == len(grid[i])-1:
            continue

        if grid[i-1][j-1] == "M" and grid[i+1][j+1] == "S" and grid[i-1][j+1] == "M" and grid[i+1][j-1] == "S":
            cnt += 1
        if grid[i-1][j-1] == "S" and grid[i+1][j+1] == "M" and grid[i-1][j+1] == "M" and grid[i+1][j-1] == "S":
            cnt += 1
        if grid[i-1][j-1] == "M" and grid[i+1][j+1] == "S" and grid[i-1][j+1] == "S" and grid[i+1][j-1] == "M":
            cnt += 1
        if grid[i-1][j-1] == "S" and grid[i+1][j+1] == "M" and grid[i-1][j+1] == "S" and grid[i+1][j-1] == "M":
            cnt += 1
print(cnt)
