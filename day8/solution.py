from functools import reduce

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

def generateTreeLists (rowIndex, colIndex, squareMatrix):
  # horizontal lists
  leftTrees = squareMatrix[rowIndex][:colIndex]
  rightTrees = squareMatrix[rowIndex][colIndex + 1:]

  # vertical lists
  topTrees = []
  for i in range(rowIndex):
    topTrees.append(squareMatrix[i][colIndex])
  bottomTrees = []
  for i in range(rowIndex + 1, len(squareMatrix)):
    bottomTrees.append(squareMatrix[i][colIndex])

  listDict = {
    "left": leftTrees,
    "right": rightTrees,
    "top": topTrees,
    "bottom": bottomTrees,
  }
  return listDict

def isVisible(rowIndex, colIndex, squareMatrix):
  # check visibility for each direction
  # if the height of the tree at the position given is >= the max height of another tree in the same row or column for at least one direction
  # return true
  positionHeight = squareMatrix[rowIndex][colIndex]

  treeListDict = generateTreeLists(rowIndex, colIndex, squareMatrix)

  leftMax = max(treeListDict["left"])
  rightMax = max(treeListDict["right"])
  topMax = max(treeListDict["top"])
  bottomMax = max(treeListDict["bottom"])

  if positionHeight > leftMax or positionHeight > rightMax or positionHeight > topMax or positionHeight > bottomMax:
    return True
  else:
    return False

def getScenicScore(height, directionDict):
  # flip the left and top lists so that they reflect the order in which the trees appear from the position being analyzed
  # rather than from the point of origin 0, 0
  directionDict["left"].reverse()
  directionDict["top"].reverse()

  scoreDict = {}

  # now to do ray-tracing from the tree outwards
  # for each direction in the dictionary, iterate over the list
  for key in directionDict:
    # start from index 0 and increment the index until an obstruction is found, or until the end of the list is reached
    i = 0
    while i < len(directionDict[key]):
      if directionDict[key][i] >= height:
        scoreDict[key] = 1 + i
        break
      else:
        i += 1
    if i == len(directionDict[key]):
      scoreDict[key] = i
    
  scoreList = scoreDict.values()
  # use a lambda function to return the multiplication of every score in the list
  final = reduce(lambda x,y: x*y, scoreList)
  return final

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

def part2(sqMatrix):
  scenicScoresList = []

  i, j = 0, 0
  for i in range(len(sqMatrix)):
    for j in range(len(sqMatrix)):
      analysisDict = generateTreeLists(i, j, sqMatrix)
      scenicScoresList.append(getScenicScore(sqMatrix[i][j], analysisDict))

  print(max(scenicScoresList)) # 211680
  return

if __name__ == "__main__":
    part1(treeMatrix)
    part2(treeMatrix)