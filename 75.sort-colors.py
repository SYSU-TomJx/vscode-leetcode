#
# @lc app=leetcode id=75 lang=python
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (41.37%)
# Total Accepted:    297.5K
# Total Submissions: 716.9K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array with n objects colored red, white or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order
# red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
#
# Note: You are not suppose to use the library's sort function for this
# problem.
#
# Example:
#
#
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#
# Follow up:
#
#
# A rather straight forward solution is a two-pass algorithm using counting
# sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
# array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?
#
#
#
class Solution(object):
    '''
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            insert_pos = i
            min_num = nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] < min_num:
                    insert_pos = j
                    min_num = nums[j]
            nums[i], nums[insert_pos] = min_num, nums[i]
    '''
    def sortColors(self, nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
        front, rear = 0, len(nums)-1

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i], nums[front] = nums[front], nums[i]
                front = front + 1
            elif nums[i] == 2:
                nums[i], nums[rear] = nums[rear], nums[i]
                rear = rear - 1
                i = i - 1



