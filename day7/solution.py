from collections import deque

inputFile = open("day7\input.txt", 'r')
data = inputFile.read().split('\n')
# print(data)

currentDir = []
# prevDir will be a stack of previous folders accessed
dirDict = {"/": 0,}
pathsAndFilesChecked = {}

for line in data:
  # each line can start with the following prefixes: 
  # '$', which will contain a command such as a 'cd' or 'ls'
  # a number, which will indicate the prescence of a single file. if the number prefix is < 100000, we will add that filesize to our total count
  # 'dir', which will indicate the prescence of a subfolder. 
  # we can actually ignore dir because the subsequent 'cd' and 'ls' lines will give us the info necessary to set up dirDict
  splitLine = line.split(" ")
  if splitLine[0] == '$':
    if splitLine[1] == 'cd':
      # we can ignore "cd /" because it only happens once
      # similarly, the '$ ls' command does not give us any information about the file sizes within the same line
      # at least not directly. the results of 'ls' will give us files and folders
      if splitLine[2] == '..':
        currentDir.pop()
      else:
        currentDir.append(splitLine[2])

  elif splitLine[0].isnumeric():
    dirString = "\\".join(currentDir)
    if dirString not in pathsAndFilesChecked:
      pathsAndFilesChecked[dirString] = []
    # if filename is not already in pathsAndFilesChecked dictionary, add it in to avoid double-counting
    # required as we do not know if puzzle input will lead us over the same filepath twice
    if splitLine[1] not in pathsAndFilesChecked[dirString]:
      pathsAndFilesChecked[dirString].append(splitLine[1])
      # iterate over all elements of current directory, which is a list of subfolders/paths in order of access
      for i in range(len(currentDir) + 1):
        # if a possible path is not included in the dictionary, initialize it to 0
        if '\\'.join(currentDir[:i]) not in dirDict.keys():
          dirDict['\\'.join(currentDir[:i])] = 0
        # then increase the value by whatever was on this line with a number first
        # this way, all parent directories are accounted for
        dirDict['\\'.join(currentDir[:i])] += int(splitLine[0])

def part1(input):
  smallDirs = {}
  for key in dirDict:
    if dirDict[key] <= 100000:
      smallDirs[key] = dirDict[key]
  # print (smallDirs)
  totalSize = sum(smallDirs.values())
  print(totalSize) # 1367870
  return

def part2(input):
  utilizedDiskSpace = max(dirDict.values())
  freeDiskSpace = 70000000 - utilizedDiskSpace
  targetFileSize = 30000000 - freeDiskSpace
  # print(utilizedDiskSpace, freeDiskSpace, targetFileSize)
  possibleDirectories = []
  for dir in dirDict.values():
    if dir >= targetFileSize:
      possibleDirectories.append(dir)
  print(min(possibleDirectories)) # 549173
  return

if __name__ == "__main__":
    part1(data)
    part2(data)