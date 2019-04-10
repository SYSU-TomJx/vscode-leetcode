#
# @lc app=leetcode id=55 lang=python
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (31.35%)
# Total Accepted:    241.1K
# Total Submissions: 767.2K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
#
# Each element in the array represents your maximum jump length at that
# position.
#
# Determine if you are able to reach the last index.
#
# Example 1:
#
#
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its
# maximum
# jump length is 0, which makes it impossible to reach the last index.
#
#
#
'''
class Solution(object):
    def solver(self, nums, start_pos, stop_pos):
        if start_pos == len(nums)-1:
            return True
        for i in range(start_pos, stop_pos+1):
            res = self.solver(nums, i, min(len(nums)-1, start_pos+nums[start_pos]))
        if res:
            return res
        return False
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.solver(nums, 0, len(nums)-1)
    def canJump(self, nums):
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True
'''
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        goal = len(nums)-1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal
