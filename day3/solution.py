inputFile = open("day3\input.txt", 'r')
data = inputFile.read().split('\n')
# print(data)

def halveStr(str):
  firstpart, secondpart = str[:int(len(str)/2)], str[int(len(str)/2):]
  return firstpart, secondpart

def part1(input):
  totalPriority = 0

  for rucksack in data:
    # getting the common item
    compartment1, compartment2 = halveStr(rucksack)
    compartment1Set = set(compartment1)
    compartment2Set = set(compartment2)
    commonItem = compartment1Set.intersection(compartment2Set)
    commonItem = list(commonItem)[0]
    
    # assigning a priority to the common item
    asciiIndex = ord(commonItem)
    # The ASCII value of the lowercase alphabet is from 97 to 122
    # The ASCII value of the uppercase alphabet is from 65 to 90.
    # a value of 1-26 should be returned for lowercase letters - take ASCII value - 96
    # a value of 27-52 should be returned for uppercase letters - take ASCII value - 38
    if asciiIndex > 90:
      priority = asciiIndex - 96
    else:
      priority = asciiIndex - 38
    totalPriority += priority
    # print(asciiIndex)
  print(totalPriority) # 7878?
  return

def part2(input):
  return

if __name__ == "__main__":
    part1(data)
    part2(data)