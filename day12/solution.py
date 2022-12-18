from string import ascii_lowercase
from heapq import heappop, heappush

inputFile = open("day12\input.txt", 'r')
data = inputFile.read().strip().split()
# print(data)

grid = [list(line) for line in data]
numRows = len(grid)
numCols = len(grid[0])

for i in range(numRows):
    for j in range(numCols):
        char = grid[i][j]
        if char == "S":
            start = i, j
        if char == "E":
            end = i, j


def height(s):
    if s in ascii_lowercase:
        return ascii_lowercase.index(s)
    if s == "S":
        return 0
    if s == "E":
        return 25


# Determine neighbors
def neighbors(i, j):
    for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ii = i + di
        jj = j + dj

        # check if neighbors are in grid
        if not (0 <= ii < numRows and 0 <= jj < numCols):
            continue
        
        # check if neighbors' height is reachable
        if height(grid[ii][jj]) <= height(grid[i][j]) + 1:
            yield ii, jj


# Dijkstra's
visited = [[False] * numCols for _ in range(numRows)]
heap = [(0, start[0], start[1])]

while True:
    steps, i, j = heappop(heap)

    if visited[i][j]:
        continue
    visited[i][j] = True

    if (i, j) == end:
        print(steps)
        break

    for ii, jj in neighbors(i, j):
        heappush(heap, (steps + 1, ii, jj))

def part1(input):
  return

def part2(input):
  return

if __name__ == "__main__":
    part1(data)
    part2(data)