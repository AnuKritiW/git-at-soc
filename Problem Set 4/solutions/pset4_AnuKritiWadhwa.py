class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myDict = dict()
        maxLen = 0
        windowStart = 0
        charNum = 0
        for char in s:
            if char in myDict:
                windowStart = max(windowStart, myDict[char] + 1)
            myDict[char] = charNum
            charNum += 1
            maxLen = max(maxLen, charNum - windowStart)
        return maxLen

def stringToString(input):
    import json

    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = stringToString(line);

            ret = Solution().lengthOfLongestSubstring(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
