from collections import defaultdict


class Solution(object):
  def wordBreak(self, s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    # Bottom-up DP: time and space O(n^2)
    if not wordDict:
        return False

    # convert to set O(size_dict)
    min_len = len(wordDict[0])
    max_len = len(wordDict[0])
    setDict = set()
    for w in wordDict:
        setDict.add(w)
        min_len = min(len(w), min_len)
        max_len = min(len(w), max_len)

    # key: (start, end), value: nil / false / true
    hashmap = defaultdict(lambda: nil)
    end = len(s)
    start = len(s) - 1

    # recursive dp solution
    def dp(start, end):
        if (start, end) in hashmap:
            return hashmap[(start, end)]

        if s[start:end] in setDict:
            if start == 0:
                return True
            if dp(start - 1, start) or dp(start - 1, end):
                hashmap[(start, end)] = True
                return True
            else:
                hashmap[(start, end)] = False
                return False

        else:
            if start == 0 or not dp(start - 1, end):
                hashmap[(start, end)] = False
                return False
            else:
                hashmap[(start, end)] = True
                return True

    # invariant, end > start
    return dp(start, end)
