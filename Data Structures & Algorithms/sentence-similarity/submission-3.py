class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        lenSentence1 = len(sentence1)
       
      
        if lenSentence1 != len(sentence2):
          return False

        lenSimilarPairs = len(similarPairs)
        wordSimilarity = dict()

        for j in range(lenSimilarPairs):
          word1, word2 = similarPairs[j]
          
          if not wordSimilarity.get(word1):
            wordSimilarity[word1] = []

          if not wordSimilarity.get(word2):
            wordSimilarity[word2] = []
          
          wordSimilarity[word1].append(word2)
          wordSimilarity[word2].append(word1)
        
        #print(wordSimilarity)


        for i in range(lenSentence1):
          sentence1Word = sentence1[i]
          sentence2Word = sentence2[i]

          matches = sentence1Word == sentence2Word
          matches = matches or (sentence1Word in wordSimilarity.get(sentence2Word, []) or sentence2Word in wordSimilarity.get(sentence1Word, []))


          if not matches:
            return False
          
        return True