inputFile = open("day3\input.txt", 'r')
data = inputFile.read().split('\n')
# print(data)

def halveStr(str):
  firstpart, secondpart = str[:int(len(str)/2)], str[int(len(str)/2):]
  return firstpart, secondpart

def groupRucksacks(input):
  groupCounter = 0
  allGroupsList = []
  singleGroupList = []

  # read rucksack - if current groupCounter is not maxed out, add the rucksack to the singleGroupList
  for rucksack in input:
    if groupCounter < 3:
      singleGroupList.append(rucksack)
      groupCounter += 1
    else:
      allGroupsList.append(singleGroupList)
      singleGroupList = [rucksack]
      groupCounter = 1
  # force-add the last group of rucksacks
  allGroupsList.append(singleGroupList)
  return allGroupsList

def getPriority(char):
  asciiIndex = ord(char)
  # The ASCII value of the lowercase alphabet is from 97 to 122
  # The ASCII value of the uppercase alphabet is from 65 to 90.
  # a value of 1-26 should be returned for lowercase letters - take ASCII value - 96
  # a value of 27-52 should be returned for uppercase letters - take ASCII value - 38
  if asciiIndex > 90:
    priority = asciiIndex - 96
  else:
    priority = asciiIndex - 38
  return priority

def part1(input):
  totalPriority = 0
  for rucksack in input:
    # getting the common item
    compartment1, compartment2 = halveStr(rucksack)
    compartment1Set = set(compartment1)
    compartment2Set = set(compartment2)
    commonItem = compartment1Set.intersection(compartment2Set)
    commonItem = list(commonItem)[0]
    
    totalPriority += getPriority(commonItem)
  print(totalPriority) # 7878
  return

def part2(input):
  groups = groupRucksacks(input)
  badgePrioritySum = 0
  for group in groups:
    badges = set(group[0]).intersection(group[1]).intersection(group[2])
    badges = list(badges)[0]
    badgePrioritySum += getPriority(badges)
  print(badgePrioritySum) # 2760
  return

if __name__ == "__main__":
    part1(data)
    part2(data)