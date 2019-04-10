#
# @lc app=leetcode id=64 lang=python
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (45.62%)
# Total Accepted:    213.4K
# Total Submissions: 466K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
#
# Input:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
#
#
#
'''
class Solution(object):
    #val_lst = []
    def dfs(self, grid, path_val, min_val, row, col):

        if row == len(grid) or col == len(grid[0]) or path_val > min_val[0]:
            return

        if row == len(grid)-1 and col == len(grid[0])-1:
            min_val[0] = min(path_val+grid[row][col], min_val[0])
            #self.val_lst.append(path_val+grid[row][col])
            return

        path_val = path_val + grid[row][col]
        self.dfs(grid, path_val, min_val, row+1, col)
        self.dfs(grid, path_val, min_val, row, col+1)
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        path_val = 0
        row = len(grid)
        col = len(grid[0])
        min_val = [999999]
        self.dfs(grid, path_val, min_val, 0, 0)
        return min_val[0]
'''
class Solution(object):
    #val_lst = []

    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        path_val = 0
        row = len(grid)
        col = len(grid[0])
        dp = [[0]*col for _ in range(row)]
        dp[0][0] = grid[0][0]
        # first rows' path
        for i in range(1, col):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for i in range(1, row):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for i in range(1, row):
            for j in range(1, col):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]

