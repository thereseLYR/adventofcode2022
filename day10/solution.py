inputFile = open("day10\input.txt", 'r')
data = inputFile.read().split('\n')
# print(data)

# two commands - noop and addx
# noop increments the cycle number by 1, while addx increments the cycle number by 2 and then increases the value of X
# split each line by space and read the first element to find which command is being given
instrList = []
for line in data:
  instrList.append(line.split(" "))
# print(instrList)

def generateCycles(list):
  cycleCounter, xVal = [ None ], 1
  # shove the current xVal into a list every cycle
  #that way, we can pull the xVal at the start of particular cycles by calling the index of xVal
  for instr in list:
    command = instr[0]
    if command == "noop":
      cycleCounter.append(xVal)
    elif command == "addx":
      cycleCounter.append(xVal)
      cycleCounter.append(xVal)
      xDelta = int(instr[1])
      xVal += xDelta
  return cycleCounter, xVal


def part1(input):
  cycles, finalX = generateCycles(instrList)
  # signal strengths are generated from cycle number * xVal for that cycle
  significantCycleVals = [20 * cycles[20], 60 * cycles[60], 100 * cycles[100], 140 * cycles[140], 180 * cycles[180], 220 * cycles[220]]
  print(sum(significantCycleVals)) # 15360
  return

def part2(input):
  cycles, finalX = generateCycles(instrList)
  # xVal controls the horizontal position of a sprite
  finalImage = ''
  for i in range(1, len(cycles)):
    # modulate spriteMiddle to keep its value < 40
    spriteMiddle = cycles[i] % 40
    spriteRange = [spriteMiddle - 1, spriteMiddle, spriteMiddle + 1]
    # need to modulate i horizontal position too, and subtract 1 to account for position index in the final image string
    if (i % 40 - 1) in spriteRange:
      finalImage += '#'
    else:
      finalImage += '.'
    # add a newline every 40 cycles
    if i % 40 == 0:
      finalImage += '\n'
  print(finalImage) # PHLHJGZA
  return

if __name__ == "__main__":
    part1(data)
    part2(data)