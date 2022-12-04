inputFile = open("day4\input.txt", 'r')
data = inputFile.read().split('\n')
# print(data)

def generate_sections(string):
  firstNum, lastNum = string.split('-')
  sections = range(int(firstNum), int(lastNum) + 1)
  return sections

def checkRangeCompleteOverlap(r1, r2):
  cond1 = r1.start in r2 and r1[-1] in r2
  cond2 = r2.start in r1 and r2[-1] in r1 
  if cond1 or cond2 is True:
    return True
  else: return False

def checkRangePartialOverlap(r1, r2):
  cond1 = r1.start in r2
  cond2 = r2.start in r1
  if cond1 or cond2 is True:
    return True
  else: return False


def part1(input):
  overlapCount = 0
  for pair in input:
    elf1Assignment, elf2Assignment = pair.split(',')
    elf1Range, elf2Range = generate_sections(elf1Assignment), generate_sections(elf2Assignment)
    completeOverlap = checkRangeCompleteOverlap(elf1Range, elf2Range)
    if completeOverlap == True:
      overlapCount += 1
  print(overlapCount) # 464
  return

def part2(input):
  overlapCount = 0
  for pair in input:
    elf1Assignment, elf2Assignment = pair.split(',')
    elf1Range, elf2Range = generate_sections(elf1Assignment), generate_sections(elf2Assignment)
    partialOverlap = checkRangePartialOverlap(elf1Range, elf2Range)
    if partialOverlap == True:
      overlapCount += 1
  print(overlapCount) # 770
  return

if __name__ == "__main__":
    part1(data)
    part2(data)