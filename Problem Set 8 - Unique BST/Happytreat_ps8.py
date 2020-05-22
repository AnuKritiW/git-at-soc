from functools import reduce

'''
Recursive with memoisation: not the best solution for time complexity
56 ms faster than 6% of Python3
'''
class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return n

        memo = {}

        '''
        Recursive way to count the number of trees rooted at `root`
        and have elements from lower+1 to upper-1 (inclusive)
        '''
        def recurse_count(root: int, upper: int, lower: int) -> int:
            if not (root < upper and root > lower):
                return 0

            if (root, upper, lower) in memo:
                return memo[(root, upper, lower)]

            if root == lower + 1 and root == upper - 1:
                return 1

            _lcount, _rcount = 0, 0
            # count left subtrees
            for r in range(lower+1, root):
                _lcount += recurse_count(r, root, lower)

            # count right subtrees
            for r in range(root+1, upper):
                _rcount += recurse_count(r, upper, root)

            memo[(root, upper, lower)] = max(1, _lcount) * max(1, _rcount)
            return memo[(root, upper, lower)]

        # counting subtrees rooted at 1...n
        return reduce((lambda x, root: x + recurse_count(root, n+1, 0)),
                      [i for i in range(1, n+1)], 0)
