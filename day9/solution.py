from functools import reduce

inputFile = open("day9\input.txt", 'r')
data = inputFile.read().split('\n')
# print(data)

# head and tail must always be adjacent = overlapping and diagonally adjacent also fulfil this criteria
# instructions for the head are given as lines
# figure out where the tail moves
# size of the grid is unknown
headLoc, tailLoc = [0, 0], [0, 0]
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

def part1(input):
  print("initial positions are:", headLoc, tailLoc)
  for line in input:
    [direction, steps] = line.split(" ")
    for i in range(int(steps)):
      
      if direction == "R":
        moveHeadR(headLoc, tailLoc)
      elif direction == "L":
        moveHeadL(headLoc, tailLoc)
      elif direction == "U":
        moveHeadUp(headLoc, tailLoc)
      elif direction == "D":
        moveHeadDown(headLoc, tailLoc)

      # print("\nheadLoc after move is:", headLoc)
      # print("tailLoc after move is:", tailLoc)

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