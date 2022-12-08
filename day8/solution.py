from collections import deque

inputFile = open("day8\input.txt", 'r')
data = inputFile.read().split('\n')
# print(data)

# the input provided can be used to form a square matrix. 
# check whether each tree is visible from a particular direction - top, bottom, left, and right
treeMatrix = []
for line in data:
  lineList = []
  for char in line:
    lineList.append(int(char))
  treeMatrix.append(lineList)

def isVisible(rowIndex, colIndex, squareMatrix):
  # check visibility for each direction
  # if the height of the tree at the position given is >= the max height of another tree in the same row or column for at least one direction
  # return true
  positionHeight = squareMatrix[rowIndex][colIndex]

  # horizontal lists
  leftTrees = squareMatrix[rowIndex][:colIndex]
  rightTrees = squareMatrix[rowIndex][colIndex + 1:]

  # veritical lists
  topTrees = []
  for i in range(rowIndex):
    topTrees.append(squareMatrix[i][colIndex])
  bottomTrees = []
  for i in range(rowIndex + 1, len(squareMatrix)):
    bottomTrees.append(squareMatrix[i][colIndex])

  # horizontal checks
  leftMax = max(leftTrees)
  rightMax = max(rightTrees)
  topMax = max(topTrees)
  bottomMax = max(bottomTrees)

  if positionHeight > leftMax or positionHeight > rightMax or positionHeight > topMax or positionHeight > bottomMax:
    return True
  else:
    return False

def part1(sqMatrix):
  # find the number of edge trees on the square matrix and automatically add them to the initial visible tree count
  numVisible = 4 * len(sqMatrix) - 4
  innerVisible = 0
  i = 1
  while i < (len(sqMatrix) - 1):
    j = 1
    while j < (len(sqMatrix) - 1):
      if isVisible(i, j, sqMatrix) == True:
        innerVisible += 1
      j += 1
    i += 1
  print(numVisible + innerVisible) # 1823
  return

def part2(input):
  return

if __name__ == "__main__":
    part1(treeMatrix)
    part2(data)