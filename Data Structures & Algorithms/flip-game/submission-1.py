class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        def findAdjacentPairs():
          adjacentPairIndex = []
          currentChar = ''
          lastChar = ''

          for i in range(len(currentState)):
            currentChar = currentState[i]
            
            if currentChar == lastChar and currentChar == '+':
              adjacentPairIndex.append(i - 1)
            
            lastChar = currentChar

          return adjacentPairIndex



        adjacentPairIndex = findAdjacentPairs()
        possibleMovesList = []

        for idx in adjacentPairIndex:
          charAtIndex = currentState[idx]
          possibleMove = currentState[0:idx] + ('--' if charAtIndex == '+' else '--') + currentState[idx + 2:]

          possibleMovesList.append(possibleMove)
          


        return possibleMovesList
