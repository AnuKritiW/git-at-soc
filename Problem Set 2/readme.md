# pset2

You are designing a new "escape" adventure that uses a rectangular grid of rooms (unit cells) with R rows and C columns. Each room has four doors oriented in the four orthogonal directions of the grid: north, south, east, and west. The doors on the border of the grid lead outside, and all of the other doors lead to other rooms.

The adventure will be played by exactly R × C players, with each player starting in a different one of the R × C rooms. Once everyone is in position and the game starts, all of the doors close, and there is a mechanical trick: one of the four doors in each room can be opened from inside the room, and the other three doors cannot be opened. This remains consistent throughout the adventure; in a given room, it is always the same door that can be opened. Notice that it is possible that a door that connects two rooms might be able to be opened from one side but not the other.

Each player moves independently of all other players. Players can only go through doors that they opened themselves, and they must close doors behind them. Each player will keep going through doors until they go through a door that leads outside (and therefore they escape), or they have made R × C moves without escaping (at which point they are considered to have failed, and they do not escape).

You want to choose which door in each room can be opened, such that exactly K of the players will be able to escape. Can you find a way to do this, or determine that it is IMPOSSIBLE?

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line containing three integers R, C, and K, as described above.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is IMPOSSIBLE if there is no solution, or POSSIBLE if there is. If there is a solution, output R more lines of C characters each, representing the grid of rooms. The j-th character on the i-th of these lines represents the room in the i-th row and j-th column of the grid; each character must be either uppercase N, S, E, or W, according to whether the door that opens from that room is the one that leads north, south, east, or west.

If multiple answers are possible, you may output any one of them.

Limits

1 ≤ T ≤ 100.

Time limit: 20 seconds per test set. (10 seconds per test run.)

Memory limit: 1GB.

1 ≤ R.

1 ≤ C.

0 ≤ K ≤ R × C.

Test set 1 (Visible)

1 ≤ (R × C) ≤ 8.

Test set 2 (Hidden)

1 ≤ (R × C) ≤ 100.

Sample

_Input_

2

2 3 2

1 1 0

_Output_

Case #1: POSSIBLE

SES

SNW

Case #2: IMPOSSIBLE


In our solution for Sample Case #1, the two players who start in the westernmost two rooms will go south until they escape, whereas the four players who start in the other four rooms will travel between those rooms in an endless clockwise circle and cannot escape.

In Sample Case #2, there is only one room, so the player can definitely escape regardless of which particular door can be opened.
