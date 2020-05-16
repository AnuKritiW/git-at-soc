from collections import defaultdict 

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 12ms faster than 99.80% of Python
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
        
        if min_len > len(s): 
            return False
        
        dp = defaultdict(bool)
        dp[len(s)] = True
        
        min_i = max(min_len - 2, -1)
        for i in range(len(s)-1, min_i, -1):
            if not dp[i+1]:
                continue
            max_j = max(i - min_len + 1, -1)
            min_j = max(i - max_len, -1)
            for j in range(max_j, min_j, -1):
                if s[j:i+1] in wordSet:
                    dp[j] = True
                    if j == 0:
                        return True
        return False
        
                