inputFile = open("day6\input.txt", 'r')
data = inputFile.read()
# print(data)

# since the start-of character marker always has a fixed length (4 characters) we can use the sliding windows technique to minimize time complexity
# within the 'viewport' of the algorithm, we further check if the 4 characters observed are all unique characters
# this can be done by chucking the characters in a set and then ensuring that the length of the set is 4
def findStartPacketMarker(signalStr, markerSize):
  markerFound, leftIndex, rightIndex = False, 0, markerSize - 1
  while(markerFound == False):
    charSet = set(signalStr[leftIndex: rightIndex + 1])
    if (len(charSet) == markerSize):
      markerFound = True
    leftIndex += 1
    rightIndex += 1
  return rightIndex, signalStr[leftIndex: rightIndex + 1]


def part1(input):
  position, marker = findStartPacketMarker(input, 4)
  # print('testing input:', input)
  print(position, marker)
  return

def part2(input):
  position, marker = findStartPacketMarker(input, 14)
  # print('testing input:', input)
  print(position, marker)
  return

if __name__ == "__main__":
    part1(data)
    part2(data)