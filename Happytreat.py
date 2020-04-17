from collections import defaultdict 

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # time: O(s^2 + n)
        # space: O(n + s)
        if not wordDict: 
            return False
        
        wordSet = set(wordDict)
        dp = defaultdict(bool)
        dp[len(s)] = True
        
        for i in range(len(s)-1, -1, -1):
            if not dp[i+1]:
                continue
            for j in range(i, -1, -1):
                if s[j:i+1] in wordSet:
                    dp[j] = True
                    if j == 0:
                        return True
        return False
        
                