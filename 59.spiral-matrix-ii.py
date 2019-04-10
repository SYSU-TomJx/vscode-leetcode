#
# @lc app=leetcode id=59 lang=python
#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (45.40%)
# Total Accepted:    129K
# Total Submissions: 283.3K
# Testcase Example:  '3'
#
# Given a positive integer n, generate a square matrix filled with elements
# from 1 to n^2 in spiral order.
#
# Example:
#
#
# Input: 3
# Output:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
#
#
#
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = []
        max_num = n*n
        for i in range(n):
            matrix.append([0]*n)
        row = 0
        col = 0
        d_row = 0
        d_col = 1
        for num in range(1,n*n+1):
            matrix[row][col] = num
            if matrix[(row+d_row)%n][(col+d_col)%n] != 0:
                d_row, d_col = d_col, -d_row
            row = row + d_row
            col = col + d_col
        return matrix





