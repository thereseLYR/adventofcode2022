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
  for roundData in input:
    shapeScore = shapeScoreMap[roundData[1]]
    outcomeScore = outcomeScoreMap[checkOutcome(roundData)] 
    roundScore = shapeScore + outcomeScore
    score += roundScore
  print(score) # expected 10404

def part2(input):
  score = 0
  for roundData in input:
    opponentPossibilities = ['A', 'B', 'C']
    opponentMove = roundData[0]
    suggestedOutcome = roundData[1]

    opponentMoveIndex = opponentPossibilities.index(opponentMove)
  
    print('roundData:', roundData)
    # print('ORIGINAL roundShapeScore:', roundShapeScore)
    
    if suggestedOutcome == 'Z': # suggest to win
      playerMoveIndex = (opponentMoveIndex + 1) % 3
      roundScore = (playerMoveIndex + 1) + 6
    elif suggestedOutcome == 'Y': # suggest to draw
      roundScore = (opponentMoveIndex + 1) + 3
    else:
      playerMoveIndex = (opponentMoveIndex + 2) % 3
      roundScore = playerMoveIndex # all other outcomes are loss
    score += roundScore
  print(score) # expected 10334

    

if __name__ == "__main__":
    part1(formattedRoundRecommendationsArr)
    part2(formattedRoundRecommendationsArr)