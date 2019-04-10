#
# @lc app=leetcode id=54 lang=python
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (29.66%)
# Total Accepted:    212K
# Total Submissions: 714.3K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
#
# Example 1:
#
#
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
class Solution(object):
    '''
    def spiralOrder(self, matrix):
        ret = []
        while matrix:
            ret += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            if matrix:
                ret += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret
    '''
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        row_nums = len(matrix)
        col_nums = len(matrix[0])
        nums = row_nums*col_nums
        visit_mat = []
        for row in range(row_nums):
            col_arr = [0]*col_nums
            visit_mat.append(col_arr)
        row = 0
        col = 0
        di = 0
        dir_r = [0,1,0,-1] # move up and down
        dir_c = [1,0,-1,0] # move right and left
        result = [] # save the result
        for i in range(nums):
            result.append(matrix[row][col])
            visit_mat[row][col] = 1 # note the visited elem
            # clock-wise
            n_row = row + dir_r[di]
            n_col = col + dir_c[di]
            if 0<=n_row<row_nums and 0<=n_col<col_nums and visit_mat[n_row][n_col]!=1:
                row = n_row
                col = n_col
            else:
            # The edge is arrived, changing the direction.
                di = (di+1)%4
                row = row + dir_r[di]
                col = col + dir_c[di]
        return result




