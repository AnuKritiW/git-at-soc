class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):
            return s
        else:
            outputString = [""] * numRows
            currPointer = -1
            direction = 1
            for x in s:
                currPointer += direction
                outputString[currPointer] += x

                if (currPointer == 0):
                    direction = 1
                elif (currPointer == numRows - 1):
                    direction = -1
                    
            return "".join(outputString)

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
