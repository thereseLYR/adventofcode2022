import ast

inputFile = open("day13\input2.txt", 'r')
data = inputFile.read().split('\n\n')
# print(data)

# each element in data is a string chunk containing a left side (line 1) and a right side (line 2)
for pair in data:
  [leftPacket, rightPacket] = pair.split('\n')

  # convert the packets from strings into lists
  leftPacket = ast.literal_eval(leftPacket)
  rightPacket = ast.literal_eval(rightPacket)

  # because the right side running out of inputs is a condition for failure, we will use the right side as the limiting range
  for i in range(len(rightPacket)):
    currLeft, currRight = leftPacket[i], rightPacket[i]
    print("types are", type(currLeft), type(currLeft))

    if type(currLeft) == type(currRight) == 'int':
      if currLeft < currRight:
        # correct order
        pass

    elif type(currLeft) == type(currRight) == 'list':
      for elem in list:
        # check if left side will run out of items
        pass
    
    else:
      # covert the int to a list and try again
      pass

  # identify if leftPacket and rightPacket are integers or lists


  # compare both integers
  # compare both lists
  # if one is an integer, convert the integer to a list that contains only the integer and re-try

def part1(input):
  return

def part2(input):
  return

if __name__ == "__main__":
    part1(data)
    part2(data)