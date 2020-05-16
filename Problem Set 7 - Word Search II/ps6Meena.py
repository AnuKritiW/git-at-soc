class Solution(object):
    def wordBreak(self, s, wordDict):
        dpArr = []

        max = len(s)
        for i in range (0, max):
          substr = s[0: i + 1]
          dpArr.append([])

          for word in wordDict:
            wordLen = len(word)
            if wordLen > i + 1:
              continue

            lastChars = s[i + 1 - wordLen: i + 1]
            if(word == lastChars and wordLen == i + 1):
              dpArr[i].append(word)
            elif(word == lastChars and len(dpArr[i - wordLen]) != 0):
              prevList = dpArr[i - wordLen]
              for e in prevList:
                dpArr[i].append(e + " " + word)

        return dpArr[max - 1]