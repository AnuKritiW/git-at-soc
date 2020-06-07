#include <bits/stdc++.h>
#define ep emplace

class Solution
{
public:
  // O(r*c) time
  // O(c) space
  int maximalRectangle(vector<vector<char>> &matrix)
  {
    if (matrix.empty() || matrix[0].empty())
    {
      return 0;
    }

    int maxArea = 0;

    // iterate for all possible histograms
    vector<int> heights(matrix[0].size(), 0);
    for (int r = 0; r < matrix.size(); r++)
    { // base of hist
      for (int c = 0; c < matrix[0].size(); c++)
      {
        heights[c] = matrix[r][c] == '1' ? heights[c] + 1 : 0; // reset height if not 1
      }
      maxArea = max(maxArea, maxRect(heights));
    }
    return maxArea;
  }

private:
  // O(n) time as n elements to pop and n to insert
  // O(n) space as n elements max in stack
  int maxRect(vector<int> &heights)
  {
    if (heights.size() == 0)
    {
      return 0;
    }

    stack<int> increasing_height;
    int maxArea = 0;
    for (int i = 0; i <= heights.size();)
    {
      // continue iterating heights
      if (increasing_height.empty() ||
          (i < heights.size() && heights[i] > heights[increasing_height.top()]))
      {
        increasing_height.ep(i);
        ++i;
      }
      else
      { // do not iterate heights (pop)
        int h = heights[increasing_height.top()];
        increasing_height.pop();
        int leftIdx = increasing_height.empty() ? -1 : increasing_height.top();
        maxArea = max(maxArea, h * (i - leftIdx - 1));
      }
    }
    return maxArea;
  }
};