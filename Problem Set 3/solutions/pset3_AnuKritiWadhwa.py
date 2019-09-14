class Solution:
    def convert(self, s: str, numRows: int) -> str:
        myList = []
        diagCounter = 0
        outputString = ''
        while s:
            if(numRows == 1):
                return s
            myList.append([])
            if (diagCounter%(numRows-1) == 0):
                diagCounter = 0
                # myList.append([])
                for x in range(0, min(numRows, len(s))):
                    myList[len(myList) - 1].append(s[0])
                    s = s[1:]
                diagCounter += 1
            else:
                for x in range(0, numRows - 1 - diagCounter):
                    myList[len(myList) - 1].append('')
                myList[len(myList) - 1].append(s[0])
                s = s[1:]
                diagCounter += 1
        for x in range(0, numRows):
            for y in myList:
                if len(y) > x:
                    outputString += y[x]
        # print(myList)
        return outputString

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
            line = next(lines)
            numRows = int(line);

            ret = Solution().convert(s, numRows)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
