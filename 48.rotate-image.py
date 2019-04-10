#
# @lc app=leetcode id=48 lang=python
#
# [48] Rotate Image
#
# https://leetcode.com/problems/rotate-image/description/
#
# algorithms
# Medium (46.92%)
# Total Accepted:    227.9K
# Total Submissions: 485.4K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Note:
#
# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.
#
# Example 1:
#
#
# Given input matrix =
# [
# ⁠ [1,2,3],
# ⁠ [4,5,6],
# ⁠ [7,8,9]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
# ⁠ [7,4,1],
# ⁠ [8,5,2],
# ⁠ [9,6,3]
# ]
#
#
# Example 2:
#
#
# Given input matrix =
# [
# ⁠ [ 5, 1, 9,11],
# ⁠ [ 2, 4, 8,10],
# ⁠ [13, 3, 6, 7],
# ⁠ [15,14,12,16]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
# ⁠ [15,13, 2, 5],
# ⁠ [14, 3, 4, 1],
# ⁠ [12, 6, 8, 9],
# ⁠ [16, 7,10,11]
# ]
#
#
#
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        dim = len(matrix)
        '''
        for i in range(s_len):
            row = i / dim
            col = i % dim
            if row == col:
                continue # ignore the elems on diag.
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        '''
        for i in range(dim):
            for j in range(i + 1, dim):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in range(dim):
            matrix[row].reverse()
        #return matrix


