from collections import deque
import re

inputFile = open("day5\input.txt", 'r')
data = inputFile.read().split('\n\n')
# print(data)

startDrawing = data[0]
rearragementProcedure = data[1]
rearragementProcedure = rearragementProcedure.split('\n')

def generateStacks(drawingStr):
  rows = drawingStr.split('\n')
  lastRow = rows.pop()
  numColumns = int(lastRow[len(lastRow) - 2])
  stacksArr = []
  for i in range(numColumns):
    stacksArr.append(deque())
  
  # add to stack corresponding to the column
  # each line has the same length due to the format of the drawing
  # thus we can check the crates by reading a specific character of the string
  # e.g. for a 35-character line in a drawing, positions to check are 2, 6, 10 etc
  # which can be generalized to a range
  positionsToCheck = range(1, 35, 4)

  for line in rows:
    # print(line)
    for pos in positionsToCheck:
      # print(line[pos])
      if line[pos] != ' ':
        stacksArrPos = int(lastRow[pos]) - 1
        stacksArr[stacksArrPos].append(line[pos])
  
  # need to reverse each stack because it was created by reading the picture top-down instead of bottom up
  # previously, the cartons on top would be at the bottom of the stack, which is incorrect
  for stack in stacksArr:
    stack.reverse()

  return stacksArr

def moveCrates(numCrates, startLoc, endLoc, stacksArr):
  i = 0
  holding = None
  while i < numCrates:
    holding = stacksArr[startLoc].pop()
    stacksArr[endLoc].append(holding)
    i += 1

def part1(input):
  stacks = generateStacks(startDrawing)

  for line in rearragementProcedure:
    # use regExp to find all numbers in a string
    numCrates, fromLocation, toLocation = re.findall(r'\b\d+\b', line)
    moveCrates(int(numCrates), int(fromLocation) - 1, int(toLocation) - 1, stacks)  
  
  resultStr = ''
  for i in stacks:
    resultStr += i.pop()
  
  print(resultStr) # DHBJQJCCW
  return

def part2(input):
  return

if __name__ == "__main__":
    part1(data)
    part2(data)