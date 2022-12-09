import copy

inputFile = open("day9\input2.txt", 'r')
data = inputFile.read().split('\n')
# print(data)

# head and tail must always be adjacent = overlapping and diagonally adjacent also fulfil this criteria
# instructions for the head are given as lines
# figure out where the tail moves
# size of the grid is unknown
tailLocSet = set()

def isDiagonal(head, tail):
  relPosition = [tail[0] - head[0], tail[1] - head[1]]
  if abs(relPosition[0]) + abs(relPosition[1]) == 2:
    return True
  else: return False

def moveHeadR(head, tail):
  # print("\ninitial head and tail:", head, tail)
  if tail[0] < head[0]:
    if head[1] != tail[1]:
      tail[1] = head[1]
    tail[0] += 1
  head[0] += 1
  # print("after move right:", head, tail)
  return head, tail

def moveHeadL(head, tail):
  # print("\ninitial head and tail:", head, tail)
  if tail[0] > head[0]:
    if head[1] != tail[1]:
      tail[1] = head[1]
    tail[0] -= 1
  head[0] -= 1
  # print("after move left:", head, tail)
  return head, tail
    
def moveHeadUp(head, tail):
  # print("\ninitial head and tail:", head, tail)
  # check if the head and tail are in same col (based on x-coord)
  if tail[1] < head[1]:
    if head[0] != tail[0]:
      tail[0] = head[0]
    tail[1] += 1
  head[1] += 1
  # print("after move up:", head, tail)
  return head, tail

def moveHeadDown(head, tail):
  # print("\ninitial head and tail:", head, tail)
  if tail[1] > head[1]:
    if head[0] != tail[0]:
      tail[0] = head[0]
    tail[1] -= 1
  head[1] -= 1
  # print("after move down:", head, tail)
  return head, tail

def moveOnce(direction, head, tail):
  if direction == "R":
    moveHeadR(head, tail)
  elif direction == "L":
    moveHeadL(head, tail)
  elif direction == "U":
    moveHeadUp(head, tail)
  elif direction == "D":
    moveHeadDown(head, tail)
  return head, tail

def part1(input):
  # print("initial positions are:", headLoc, tailLoc)
  headLoc, tailLoc = [0, 0], [0, 0]
  for line in input:
    [direction, steps] = line.split(" ")
    for i in range(int(steps)):
      moveOnce(direction, headLoc, tailLoc)
      tailLocStr = str(tailLoc[0]) + str(tailLoc[1])
      tailLocSet.add(tailLocStr)
      # print(len(tailLocSet))

  # print("final positions are:", headLoc, tailLoc)
  # print("tail has visited:", tailLocSet)
  print(len(tailLocSet)) # 6494
  return

def part2(input):
  return

if __name__ == "__main__":
    part1(data)
    part2(data)