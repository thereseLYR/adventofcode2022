inputFile = open("day1\input.txt", 'r')
data = inputFile.read().split('\n\n')

def getTotalCalorieList(input):
  formattedTotalCalorieList = []
  i = 0
  while i < len(data):
    granularSplit = data[i].split('\n')
    sum = 0
    for j in granularSplit:
      sum += int(j)
    formattedTotalCalorieList.append(sum)
    i += 1
  return formattedTotalCalorieList

def part1(input):
  calorieList = getTotalCalorieList(data)
  print(max(calorieList))
  return

def part2(input):
  sortedCalorieList = sorted(getTotalCalorieList(data), reverse=True)
  topThree = sortedCalorieList[0:3]
  print(sum(topThree))
  return

if __name__ == "__main__":
    part1(data)
    part2(data)