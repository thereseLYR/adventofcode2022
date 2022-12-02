# A for Rock, B for Paper, and C for Scissors (Opponent)
# X for Rock, Y for Paper, and Z for Scissors (Player)

outcomesMap = {
  'win': [['A', 'Y'], ['B', 'Z'], ['C', 'X']],
  'draw': [['A', 'X'], ['B', 'Y'], ['C', 'Z']],
}

shapeScoreMap = {
  "X": 1,
  "Y": 2,
  "Z": 3 
}

outcomeScoreMap = {
  "win": 6,
  "lose": 0,
  "draw": 3
}

inputFile = open("day2\input.txt", 'r')
data = inputFile.read().split('\n')

formattedRoundRecommendationsArr = []
i = 0
while i < len(data):
  roundArr = data[i].split(" ")
  formattedRoundRecommendationsArr.append(roundArr)
  i += 1
# print(formattedRoundRecommendationsArr)

def checkOutcome(arr):
  if arr in outcomesMap['win']:
    return 'win'
  elif arr in outcomesMap['draw']:
    return 'draw'
  else: return 'lose'


def part1(input):
  score = 0
  print(score)
  for roundData in input:
    shapeScore = shapeScoreMap[roundData[1]]
    outcomeScore = outcomeScoreMap[checkOutcome(roundData)] 

    # print(roundData)
    # print('gained shape:', shapeScore)
    # print(checkOutcome(roundData),'gained outcome', outcomeScore)
    # print('total score', shapeScore + outcomeScore)

    roundScore = shapeScore + outcomeScore
    score += roundScore
    # print(score)
  print(score) # currently getting 10233
    

if __name__ == "__main__":
    part1(formattedRoundRecommendationsArr)
    # part2(data)