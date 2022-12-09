import copy

inputFile = open("day9\input.txt", 'r')
data = inputFile.read().split('\n')
# print(data)

parsedInstr = []
for line in data:
  parsedInstr.append(line.split(" "))
# print(parsedInstr)

movesDict= {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1)}

class Rope:
  def __init__(self, knots):
    self.knots = [(0, 0) for _ in range(knots)]
    self.tailPositions = set()
  
  @property # define as property so that the head coordinates can be retrieved and updated by moveHead
  def head(self):
    return self.knots[0]
  
  # other than creating Rope as a class with its own properties and methods, 
  # the other important part of this method is separating the head and tail movements
  # the previous implementation hardcoded the movement of a single tail, which made it hard to scale to more knots
  # instead, we now mathematically generalize the relative position of the tail from the head and then move it
  def moveHead(self, dir):
    d_x, d_y = movesDict[dir]
    self.knots[0] = (self.head[0] + d_x, self.head[1] + d_y)
  
  def moveTail(self):
    for index, knotCoords in enumerate(self.knots[1:]):
      dxHead = self.knots[index][0] - knotCoords[0]
      dyHead = self.knots[index][1] - knotCoords[1]

      # if knot is no longer adjacent or diagonally adjacent (dx or dy >1), it will need to be moved
      if abs(dxHead) > 1 or abs(dyHead) > 1:
        dxTail = dxHead if abs(dxHead == 1) else dxHead // 2
        dyTail = dyHead if abs(dyHead == 1) else dyHead // 2
        # change the position of the subsequent knot, i + 1
        self.knots[index+1] = (knotCoords[0] + dxTail, knotCoords[1] + dyTail)
        
  def logTailPos(self):
    # add the positon of the last knot to the set of positions
    self.tailPositions.add(self.knots[-1])

  def moveOnce(self, instr):
    for _ in range(int(instr[1])): # instr[1]) is the number of steps to move in a direction
      self.moveHead(instr[0]) # instr[0] is string that indicates the direction to move 
      self.moveTail()
      self.logTailPos()
  
  def moveAllInstr(self, instrList):
    for instr in instrList:
      self.moveOnce(instr)

def part1(input):
  r = Rope(2)
  r.moveAllInstr(input)
  # print(r.tailPositions)
  print(len(r.tailPositions)) # 6494
  return

def part2(input):
  r = Rope(10)
  r.moveAllInstr(input)
  # print(r.tailPositions)
  print(len(r.tailPositions)) # 2691
  return

if __name__ == "__main__":
    part1(parsedInstr)
    part2(parsedInstr)