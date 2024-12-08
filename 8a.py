from itertools import combinations

"""
For all nCr(n, 2) unique lines through n points there are 2k ideal points.
"""

antennas = {}
grid = [line.strip() for line in open("8.txt")]
for i, line in enumerate(grid):
    for j, ch in enumerate(line):
        if ch != '.':
            if ch not in antennas:
                antennas[ch] = [(i, j)]
            else:
                antennas[ch].append((i, j))

antinodes = set()
for freq in antennas:
    for a, b in combinations(antennas[freq], 2):
        """
a - d = b - 2d
a + d = b
d = b - a
        """
        diff = (b[0] - a[0], b[1] - a[1])

        an1 = (b[0] + diff[0], b[1] + diff[1])
        an2 = (a[0] - diff[0], a[1] - diff[1])
        if an1[0] >= 0 and an1[0] < len(grid) and an1[1] >= 0 and an1[1] < len(grid[0]):
            antinodes.add(an1)
        if an2[0] >= 0 and an2[0] < len(grid) and an2[1] >= 0 and an2[1] < len(grid[0]):
            antinodes.add(an2)

print(len(antinodes))
