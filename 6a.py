obstacles = []
pos = None
grid = [line.strip() for line in open("6.txt").read().split("\n")[:-1]]
for i, line in enumerate(grid):
    for j, ch in enumerate(line):
        if ch == '#':
            obstacles.append((i, j))
        elif ch == '^':
            pos = [i, j]

visited = set()
direction = "up"
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

print(len(visited))

# swept = 0
# direction = "up"
# while True:
#     if direction == "up":
#         stop = None
#         for ob in obstacles:
#             if ob[0] < pos[0] and ob[1] == pos[1] and (stop is None or ob[0] > stop[0]):
#                 stop = [ob[0] + 1, ob[1]]
#         if stop is None:
#             break
#         print(stop, swept)
#         swept += pos[0] - stop[0]
#         direction = "right"
#     elif direction == "right":
#         stop = None
#         for ob in obstacles:
#             if ob[1] > pos[1] and ob[0] == pos[0] and (stop is None or ob[1] < stop[1]):
#                 stop = [ob[0], ob[1] - 1]
#         if stop is None:
#             break
#         print(stop, swept)
#         swept += stop[1] - pos[1]
#         direction = "down"
#     elif direction == "down":
#         stop = None
#         for ob in obstacles:
#             if ob[0] > pos[0] and ob[1] == pos[1] and (stop is None or ob[0] < stop[0]):
#                 stop = [ob[0] - 1, ob[1]]
#         if stop is None:
#             break
#         print(stop, swept)
#         swept += stop[0] - pos[0]
#         direction = "left"
#     elif direction == "left":
#         stop = None
#         for ob in obstacles:
#             if ob[1] < pos[1] and ob[0] == pos[0] and (stop is None or ob[1] > stop[1]):
#                 stop = [ob[0], ob[1] + 1]
#         if stop is None:
#             break
#         print(stop, swept)
#         swept += pos[1] - stop[1]
#         direction = "up"
#     pos = stop
# print(swept)
