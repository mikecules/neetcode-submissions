class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def getStrFrequencyDict(s: str) -> dict[int]:
            strFreqDict = dict()

            for c in s:
                if strFreqDict.get(c, None) is None:
                    strFreqDict[c] = 0
                
                strFreqDict[c] += 1

            return strFreqDict

        
        dictStrS, dictStrT = getStrFrequencyDict(s), getStrFrequencyDict(t)

        for c in s:
            sFreq = dictStrS.get(c, None)
            tFreq = dictStrT.get(c, None)

            if sFreq is None or tFreq is None:
                return False

            elif sFreq != tFreq:
                return False

            dictStrS[c] -= 1
            dictStrT[c] -= 1
            
            if dictStrS[c] == 0:
                del dictStrS[c]

            if dictStrT[c] == 0:
                del dictStrT[c]

            
        return len(dictStrS.keys()) == 0 and len(dictStrT.keys()) == 0
