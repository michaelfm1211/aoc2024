grid = [line.strip() for line in open("4.txt")]
cnt = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != 'X':
            continue

        # horizontal right
        try:
            if grid[i][j] == "X" and grid[i][j+1] == "M" and grid[i][j+2] == "A" and grid[i][j+3] == "S":
                cnt += 1
                print(cnt, "HR", i, j)
        except Exception:
            pass
        # horizontal left
        try:
            if j-3>=0 and grid[i][j] == "X" and grid[i][j-1] == "M" and grid[i][j-2] == "A" and grid[i][j-3] == "S":
                cnt += 1
                print(cnt, "HL", i, j)
        except Exception:
            pass
        # vertical down
        try:
            if grid[i][j] == "X" and grid[i+1][j] == "M" and grid[i+2][j] == "A" and grid[i+3][j] == "S":
                cnt += 1
                print(cnt, "VD", i, j)
        except Exception:
            pass
        # vertical up
        try:
            if i-3>=0 and grid[i][j] == "X" and grid[i-1][j] == "M" and grid[i-2][j] == "A" and grid[i-3][j] == "S":
                cnt += 1
                print(cnt, "VU", i, j)
        except Exception:
            pass
        # diagonal down right
        try:
            if grid[i][j] == "X" and grid[i+1][j+1] == "M" and grid[i+2][j+2] == "A" and grid[i+3][j+3] == "S":
                cnt += 1
                print(cnt, "DDR", i, j)
        except Exception:
            pass
        # diagonal up right
        try:
            if i-3>=0 and grid[i][j] == "X" and grid[i-1][j+1] == "M" and grid[i-2][j+2] == "A" and grid[i-3][j+3] == "S":
                cnt += 1
                print(cnt, "DUR", i, j)
        except Exception:
            pass
        # diagonal down left
        try:
            if j-3>=0 and grid[i][j] == "X" and grid[i+1][j-1] == "M" and grid[i+2][j-2] == "A" and grid[i+3][j-3] == "S":
                cnt += 1
                print(cnt, "DDL", i, j)
        except Exception:
            pass
        # diagonal up left
        try:
            if i-3>=0 and j-3>=0 and grid[i][j] == "X" and grid[i-1][j-1] == "M" and grid[i-2][j-2] == "A" and grid[i-3][j-3] == "S":
                cnt += 1
                print(cnt, "DUL", i, j)
        except Exception:
            pass

print(cnt)
