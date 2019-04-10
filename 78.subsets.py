#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (51.09%)
# Total Accepted:    338.9K
# Total Submissions: 659K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
#
#
class Solution(object):
    def solver(self, nums, index, res, item, k):
        #if item not in res:
        res.append(item)
        if k == 0:
            return
        for i in range(index, len(nums)):
            self.solver(nums, i+1, res, item+[nums[i]], k-1)
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.solver(nums, 0, res, [], len(nums))
        return res



