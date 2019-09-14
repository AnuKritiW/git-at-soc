#INCOMPLETE

def main():
  f = open("testcase1.txt")
  T = int(f.readline())

  while T > 0:
      testcase = f.readline()
      a = []
      a = map(int, line.split(" "))
      R = a[0]
      C = a[1]
      K = a[2]
      T -= 1
      solve(R, C, K)

def solve(rows, columns, players):
    if (players > rows * columns || players < 0 || rows < 0 || columns < 0 || players == (rows*columns - 1)):
        return False

    # grid = [['0'] * rows for i in range(columns)]
    grid = [['0'] * rows * columns]

    for i in range(players):
        grid[i] = 'N'

    if columns == 1:
        for i in range(players, len(grid)):
            grid[i] = 'S'
        grid[len(grid) - 1] = 'N' #make the last one north
        return True

    if((len(grid) - players) > columns):
        for i in range(players, len(grid) - columns):
            grid[i] = 'S'

    lastCell = grid[length] - columns
    if((len(grid) - players) < columns || rows == 1):
        lastCell = players

    for i in range(lastCell, len(grid) - 1):
        grid[i] = 'E'

    # point the last one west to create a loop
    grid[len(grid) - 1] = 'W'
    return True;
