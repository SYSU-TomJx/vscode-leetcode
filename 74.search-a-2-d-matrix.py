#
# @lc app=leetcode id=74 lang=python
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (34.68%)
# Total Accepted:    210.6K
# Total Submissions: 606.9K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
#
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
#
#
# Example 1:
#
#
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 3
# Output: true
#
#
# Example 2:
#
#
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 13
# Output: false
#
#
class Solution(object):
    '''
    def searchMatrix(self, matrix, target):
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1

        while low <= high:
            mid = (low + high) / 2
            num = matrix[mid / cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1

        return False
    '''
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:
            return False
        row = len(matrix)
        col = len(matrix[0])
        loc_row = 0
        loc_col = 0
        if matrix[0] == [] or target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        for i, lst in enumerate(matrix):
            if lst == []:
                return False
            if target>=matrix[i][0] and target<=matrix[i][-1]:
                front = 0
                rear = col
                while front <= rear:
                    mid = (front+rear)/2
                    if target == matrix[i][mid]:
                        return True
                    if target < matrix[i][mid]:
                        rear = mid - 1
                    elif target > matrix[i][mid]:
                        front = mid + 1

        return False

