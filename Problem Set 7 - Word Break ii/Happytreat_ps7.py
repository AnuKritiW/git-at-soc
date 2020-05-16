from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # 32 ms, faster than 98.68% of Python3

        if not wordDict:
            return []

        wordSet = set()
        max_len = len(wordDict[0])
        min_len = len(wordDict[0])
        for word in wordDict:
            wordSet.add(word)
            max_len = max(max_len, len(word))
            min_len = min(min_len, len(word))

        dp = defaultdict(list)

        first_iter = False  # break if first_iter returns no word
        for i in range(len(s)-1, -1, -1):

            if not dp[i+1] and i != len(s)-1:
                continue

            if i != len(s)-1 and not first_iter:
                return []

            max_j = max(i - min_len + 1, -1)
            min_j = max(i - max_len, -1)
            for j in range(max_j, min_j, -1):
                frag = s[j:i+1]

                if frag in wordSet:
                    if i == len(s)-1:
                        dp[j].append([frag])
                        first_iter = True
                    else:
                        dp[j].append([frag, i+1])

        def getFragments(idx: int) -> List[List[str]]:
            output = []
            for sent in dp[idx]:
                if len(sent) == 1:
                    output.append([sent[0]])
                    continue

                for i in getFragments(sent[1]):
                    frags = [sent[0]] + i
                    output.append(frags)
            return output

        return map(lambda l: " ".join(l), getFragments(0))
