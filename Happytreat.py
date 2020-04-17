from collections import defaultdict 

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 16ms faster than 98.32% of Python
        # time: O(s^2 + n)
        # space: O(n + s)
        if not wordDict: 
            return False
        
        wordSet = set()
        max_len = len(wordDict[0])
        min_len = len(wordDict[0])
        for word in wordDict: 
            wordSet.add(word)
            max_len = max(max_len, len(word))
            min_len = min(min_len, len(word))
            
        dp = defaultdict(bool)
        dp[len(s)] = True
        
        for i in range(len(s)-1, -1, -1):
            if not dp[i+1]:
                continue
            max_j = i - min_len + 1
            min_j = max(i - max_len, -1)
            for j in range(max_j, min_j, -1):
                if s[j:i+1] in wordSet:
                    dp[j] = True
                    if j == 0:
                        return True
        return False