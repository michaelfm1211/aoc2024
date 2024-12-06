obstacles = []
start = None
grid = [line.strip() for line in open("6.txt").read().split("\n")[:-1]]
for i, line in enumerate(grid):
    for j, ch in enumerate(line):
        if ch == '#':
            obstacles.append((i, j))
        elif ch == '^':
            start = (i, j)


def is_cyclic(start, obs):
    seen = set()
    pos = list(start)
    direction = "up"
    while True:
        if direction == "up":
            stop = None
            for ob in obs:
                if ob[0] < pos[0] and ob[1] == pos[1] and (stop is None or ob[0] > stop[0]):
                    stop = ob
            if stop is None:
                return False
            stop = [stop[0] + 1, stop[1]]
            if (stop[0], stop[1], direction) in seen:
                return True
            seen.add((stop[0], stop[1], direction))
            direction = "right"
        elif direction == "right":
            stop = None
            for ob in obs:
                if ob[1] > pos[1] and ob[0] == pos[0] and (stop is None or ob[1] < stop[1]):
                    stop = ob
            if stop is None:
                return False
            stop = [stop[0], stop[1] - 1]
            if (stop[0], stop[1], direction) in seen:
                return True
            seen.add((stop[0], stop[1], direction))
            direction = "down"
        elif direction == "down":
            stop = None
            for ob in obs:
                if ob[0] > pos[0] and ob[1] == pos[1] and (stop is None or ob[0] < stop[0]):
                    stop = ob
            if stop is None:
                return False
            stop = [stop[0] - 1, stop[1]]
            if (stop[0], stop[1], direction) in seen:
                return True
            seen.add((stop[0], stop[1], direction))
            direction = "left"
        elif direction == "left":
            stop = None
            for ob in obs:
                if ob[1] < pos[1] and ob[0] == pos[0] and (stop is None or ob[1] > stop[1]):
                    stop = ob
            if stop is None:
                return False
            stop = [stop[0], stop[1] + 1]
            if (stop[0], stop[1], direction) in seen:
                return True
            seen.add((stop[0], stop[1], direction))
            direction = "up"
        pos = stop
    print()


# find the path taken
visited = set()
direction = "up"
pos = list(start)
while pos[0] > 0 and pos[0] < len(grid) and pos[1] > 0 and pos[1] < len(grid[0]):
    visited.add(tuple(pos))
    
    nextpos = [pos[0], pos[1]]
    if direction == "up":
        nextpos[0] -= 1
    elif direction == "right":
        nextpos[1] += 1
    elif direction == "down":
        nextpos[0] += 1
    elif direction == "left":
        nextpos[1] -= 1

    stop = None
    for ob in obstacles:
        if ob == tuple(nextpos):
            stop = ob
            break
    if stop is None:
        pos = nextpos
    else:
        if direction == "up":
            direction = "right"
        elif direction == "right":
            direction = "down"
        elif direction == "down":
            direction = "left"
        elif direction == "left":
            direction = "up"
print("path length: ", len(visited))

# try adding an obstacle on each part of the path and check for cycles
cnt = 0
for i, j in list(visited):
    if (i, j) == start:
        continue

    if is_cyclic(start, obstacles + [(i, j)]):
        print((i, j))
        cnt += 1
print(cnt)
